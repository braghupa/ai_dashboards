from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic
import os

app = Flask(__name__)
CORS(app)  # allows your HTML frontend to call this server

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
print("API KEY LOADED:", os.environ.get("ANTHROPIC_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    try:
        body = request.json
        message = body.get("message", "")
        system = body.get("system", "You are a helpful assistant.")

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=200,
            system=system,
            messages=[{"role": "user", "content": message}]
        )

        return jsonify({"text": response.content[0].text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
