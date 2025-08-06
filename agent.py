import sys
print("Python version:", sys.version)
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os

app = Flask(__name__)
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

def start(update, context):
    update.message.reply_text("🤖 Ferme IA Ultra opérationnelle !")

dispatcher.add_handler(CommandHandler("start", start))

@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "Ferme IA Ultra prête."

if __name__ == "__main__":
    app.run(debug=True)
