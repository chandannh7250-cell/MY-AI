from flask import Flask, request, jsonify
from myai_library.engine import generate_code, search_code

app = Flask(__name__)

@app.route("/")
def home():
    return "MY-AI is Live! Use /ask?prompt=hello"

@app.route("/ask")
def ask():
    prompt = request.args.get("prompt", "")
    result = generate_code(prompt)
    if not result:
        result = search_code(prompt)
    return jsonify({"prompt": prompt, "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
