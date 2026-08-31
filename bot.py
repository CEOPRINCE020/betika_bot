import os, random, threading
from datetime import datetime
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN=os.getenv("TOKEN","8849122687:AAEK6k4q8QMW__AJ3sXSgzc-4nZRej4D-PQ")
CHAT_ID=None

flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return "GODYSTE V2 24/7 LIVE - Bot Active!"

def analyze_matches():
    pool=[("Man City vs Brentford - 1X","Form iko juu","1.35"),("Arsenal vs Fulham - Over 1.5","Attack kali","1.40"),("Liverpool vs Wolves - Over 1.5","Goli lazima","1.32"),("Real Madrid vs Getafe - 1X","Bernabeu ngumu","1.28"),("Bayern vs Augsburg - 1","Allianz fortress","1.25"),("PSG vs Lorient - Over 1.5","Messi effect","1.33")]
    random.shuffle(pool)
    ticket=[]; total=1.0
    for m,r,o in pool:
        if len(ticket)>=7: break
        total*=float(o)
        if total>2.9: total/=float(o); continue
        ticket.append(f"{len(ticket)+1}. {m} - {r} @ {o}")
    if total<2.0: total=round(random.uniform(2.0,2.8),2)
    return ticket, round(total,2)

async def send_daily_tips(c):
    global CHAT_ID
    if not CHAT_ID: return
    ticket,odds=analyze_matches()
    today=datetime.now().strftime("%d %b %Y")
    msg=f"🔥 GODYSTE MASTERMIND V2 🔥\n\n{today}\n\n" + "\n".join(ticket) + f"\n\nTotal Odds: {odds}"
    await c.bot.send_message(chat_id=CHAT_ID,text=msg,parse_mode='Markdown')

async def start(u,c):
    global CHAT_ID
    CHAT_ID=u.effective_chat.id
    await u.message.reply_text("🔥 V2 LIVE! Ume-activate 4x daily! /tip")
    await send_daily_tips(c)

async def tip(u,c):
    global CHAT_ID
    CHAT_ID=u.effective_chat.id
    await send_daily_tips(c)

def run_bot():
    app=ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CommandHandler("tip",tip))
    app.job_queue.run_repeating(send_daily_tips,interval=21600,first=10)
    print("V2 BOT THREAD INAANZA...")
    app.run_polling()

threading.Thread(target=run_bot, daemon=True).start()
print("Flask main ina-start...")
flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT",10000)))
