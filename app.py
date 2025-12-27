from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# ---------- DATABASE ----------
def get_db_connection():
    conn = sqlite3.connect("contacts.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_table()

# ---------- ROUTES ----------
@app.route("/", methods=["GET"])
def home():
    return "Backend with Database is running"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json(force=True)
    name = data.get("name")
    email = data.get("email")

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO contacts (name, email) VALUES (?, ?)",
        (name, email)
    )
    conn.commit()
    conn.close()

    print("Saved to DB:", name, email)

    return jsonify({"message": "Data saved successfully!"}), 200

# 👉 ADMIN API (ALL DATA)
@app.route("/all", methods=["GET"])
def all_data():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM contacts").fetchall()
    conn.close()

    result = []
    for r in rows:
        result.append({
            "id": r["id"],
            "name": r["name"],
            "email": r["email"]
        })

    return jsonify(result), 200

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)