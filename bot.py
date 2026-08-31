import threading
import os
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "8849122687:AAEK6k4q8QMW__AJ3sXSgzc-4nZRej4D-PQ")

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Live! V2 - Mastermind"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 MASTERMIND V2 LIVE! Bot iko sawa kabisa! \n\nAndika /help kuona commands.")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/start - Anzisha bot\n/help - Msaada")

def run_bot():
    print("V2 BOT THREAD INAANZA...", flush=True)
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_cmd))
    print("Bot @Mastermind is polling...", flush=True)
    application.run_polling(drop_pending_updates=True)

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    print("Flask main ina-start...", flush=True)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
