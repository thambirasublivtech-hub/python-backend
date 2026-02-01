from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASS"),
    database=os.environ.get("DB_NAME")
)

cursor = db.cursor(dictionary=True)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (data["name"], data["email"])
    )
    db.commit()
    return jsonify({"message": "Saved successfully"})

@app.route("/users", methods=["GET"])
def get_users():
    cursor.execute("SELECT * FROM users")
    return jsonify(cursor.fetchall())

if __name__ == "__main__":
    app.run()
