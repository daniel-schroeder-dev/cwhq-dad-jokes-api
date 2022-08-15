from flask import Flask, jsonify
from jokes import get_joke
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/random/jokes")
def get_random_joke():
    return jsonify(get_joke())
