from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# 🔹 Database connection
def get_db_connection():
    conn = sqlite3.connect("contacts.db")
    conn.row_factory = sqlite3.Row
    return conn

# 🔹 Create table (first time only)
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

@app.route("/")
def home():
    return "Backend with Database is running"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    # Save data to DB
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO contacts (name, email) VALUES (?, ?)",
        (name, email)
    )
    conn.commit()
    conn.close()

    print("Saved to DB:", name, email)

    return jsonify({"message": "Data saved successfully!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)