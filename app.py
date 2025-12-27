from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    # Terminal me show
    print("Name:", name)
    print("Email:", email)

    # Data file me save
    with open("data.txt", "a") as f:
        f.write(f"{name}, {email}\n")

    return jsonify({"message": "congratulations"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)