# app.py
from flask import Flask, request, jsonify
from chatbot.bot.py import get_chatbot_response

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message")
    if not message:
        return jsonify({"error": "No message provided"}), 400
    response = get_chatbot_response(message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
