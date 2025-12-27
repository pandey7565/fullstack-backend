from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 👈 ye OPTIONS issue solve karega

@app.route("/", methods=["GET"])
def home():
    return "Backend running"

@app.route("/submit", methods=["POST", "OPTIONS"])
def submit():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    print("Name:", name)
    print("Email:", email)

    return jsonify({"message": "Congratulations! Data received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)