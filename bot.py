import os, threading, asyncio
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8849122687:AAEK6k4q8QMW__AJ3sXSgzc-4nZRej4D-PQ"
app = Flask(__name__)

@app.route('/')
def home():
    return "MASTERMIND V2 LIVE - OK"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 MASTERMIND V2 LIVE! Iko sawa bro! Umefanikiwa!")

def run_bot():
    print("BOT INAANZA TENA...", flush=True)
    async def main():
        app_bot = ApplicationBuilder().token(TOKEN).build()
        app_bot.add_handler(CommandHandler("start", start))
        print("Polling...", flush=True)
        await app_bot.run_polling(drop_pending_updates=True)
    asyncio.run(main())

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
