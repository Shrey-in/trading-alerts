from flask import Flask, request
import requests
from config import BOT_TOKEN, CHAT_ID

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    message = f"📈 TradingView Alert\n\n{data}"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    return {"status": "success"}

if __name__ == "__main__":
    app.run(port=5000)