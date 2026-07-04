from flask import Flask, request
import requests
from config import BOT_TOKEN, CHAT_ID

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    symbol = data.get("symbol", "Unknown")
    price = data.get("price", "Unknown")
    action = data.get("action", "Unknown")
    timeframe = data.get("timeframe", "Unknown")

    message = f"""
🚨 TradingView Alert

📈 Symbol: {symbol}
💰 Price: {price}
📊 Action: {action}
⏰ Timeframe: {timeframe}
"""

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