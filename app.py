from flask import Flask, request, jsonify
from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL

app = Flask(__name__)
TelegramBot.init_webhook(TELEGRAM)

@app.route('/webhook')
def index():
    pass

if __name__ == '__main__':
    app.run(host='locahost', port=8080, debug=True)

