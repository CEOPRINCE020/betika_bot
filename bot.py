import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8849122687:AAEK6k4q8QMW__AJ3sXSgzc-4nZRej4D-PQ"
app = Flask(__name__)

@app.route('/')
def home(): return "Bot Live"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 MASTERMIND LIVE! Iko sawa!")

def run_bot():
    print("BOT INAANZA...", flush=True)
    a = ApplicationBuilder().token(TOKEN).build()
    a.add_handler(CommandHandler("start", start))
    a.run_polling(drop_pending_updates=True)

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
