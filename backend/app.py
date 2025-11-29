from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from parser import judgeText
from flask import Flask, request, jsonify
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  # allow all origins for development

@app.route("/api/receive", methods=["POST"])
def receive_text():
    data = request.get_json()
    print("Received text:", data.get("text"))
    return jsonify({"success": True})


@app.route("/api/receiveToJudge", methods=["POST"])
def beJudged():
    data = request.get_json()
    inp = data.get("text", "")
    judgment = judgeText(inp)
    return jsonify({"judgment": judgment})

if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)