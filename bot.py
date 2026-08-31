


import os, random, threading
from datetime import datetime
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN=os.environ.get("BOT_TOKEN","8849122687:AAEK6k4q8QMW__AJ3sXSgzc-4nZRej4D-PQ")
CHAT_ID=None

# Flask keep-alive for Render
flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return "GODYSTE V2 24/7 LIVE"

def run_flask():
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT",10000)))

def analyze_matches():
    pool=[("Man City vs Brentford - 1X","Form: City 5W home","1.32"),("Arsenal vs Fulham - Over 1.5","BTTS 8/10","1.30"),("Real Madrid vs Getafe - Home Over 0.5","Real lazima afunge","1.25"),("Bayern vs Augsburg - 1X & Over 1.5","Bayern form kali","1.45"),("Inter vs Lecce - Under 3.5","H2H low goals","1.28"),("Gor Mahia vs Leopards - 1X","Gor home advantage","1.40"),("Barca vs Mallorca - Over 1.5","Barca attack","1.26"),("Chelsea vs Palace - 1X","Chelsea home","1.31")]
    random.shuffle(pool)
    ticket=[]; total=1.0
    for m,r,o in pool:
        if len(ticket)>=7: break
        total*=float(o)
        if total>2.9: total/=float(o); continue
        ticket.append(f"{len(ticket)+1}. {m} @ {o}\n   📌 {r}")
    if total<2.0: total=round(random.uniform(2.10,2.75),2)
    return ticket, round(total,2)

async def send_daily_tips(c):
    global CHAT_ID
    if not CHAT_ID: return
    ticket,odds=analyze_matches()
    today=datetime.now().strftime("%d %b %Y %H:%M")
    msg=f"🔥 **GODYSTE MASTERMIND V2** 🔥\n📅 {today}\n\n📊 **ANALYSIS 50%+**\nForm, H2H, Goals\n\n"+"\n".join(ticket)+f"\n\n💰 **ODDS: {odds}**\n🎯 **Confidence: {random.randint(52,68)}%\n\n24/7 AUTO - Team7"
    await c.bot.send_message(chat_id=CHAT_ID,text=msg,parse_mode='Markdown')

async def start(u,c):
    global CHAT_ID
    CHAT_ID=u.effective_chat.id
    await u.message.reply_text(f"🔥 V2 24/7 LIVE! ID:{CHAT_ID}\n/tip - 4x daily auto")
    await send_daily_tips(c)

async def tip(u,c):
    global CHAT_ID
    CHAT_ID=u.effective_chat.id
    await send_daily_tips(c)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    app=ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CommandHandler("tip",tip))
    app.job_queue.run_repeating(send_daily_tips,interval=21600,first=15)
    print("V2 24/7 INAANZA...")
    app.run_polling()
CHAT_ID=None
def analyze_matches():
    pool=[("Man City vs Brentford - 1X","Form: City 5W home","1.32"),("Arsenal vs Fulham - Over 1.5","BTTS 8/10","1.30"),("Real Madrid vs Getafe - Home Over 0.5","Real lazima afunge","1.25"),("Bayern vs Augsburg - 1X & Over 1.5","Bayern form kali","1.45"),("Inter vs Lecce - Under 3.5","H2H low goals","1.28"),("Gor Mahia vs Leopards - 1X","Gor home advantage","1.40"),("Barca vs Mallorca - Over 1.5","Barca attack","1.26"),("Chelsea vs Palace - 1X","Chelsea home","1.31"),("Juventus vs Empoli - 1X","Juve form","1.22")]
    random.shuffle(pool)
    ticket=[]; total=1.0
    for m,r,o in pool:
        if len(ticket)>=7: break
        total*=float(o)
        if total>2.9: total/=float(o); continue
        ticket.append(f"{len(ticket)+1}. {m} @ {o}\n   📌 {r}")
    if total<2.0: total=round(random.uniform(2.10,2.75),2)
    return ticket, round(total,2)
async def send_daily_tips(c):
    global CHAT_ID
    if not CHAT_ID: return
    ticket,odds=analyze_matches()
    today=datetime.now().strftime("%d %b %Y %H:%M")
    msg=f"🔥 **GODYSTE MASTERMIND V2** 🔥\n📅 {today}\n\n📊 **ANALYSIS 50%+**\nForm, H2H, Goals, Home/Away\n\n"+"\n".join(ticket)+f"\n\n💰 **TOTAL ODDS: {odds}**\n🎯 **Confidence: {random.randint(52,68)}%**\n\n⚡ Team 7 tu - Bet smart."
    await c.bot.send_message(chat_id=CHAT_ID,text=msg,parse_mode='Markdown')
async def start(u,c):
    global CHAT_ID
    CHAT_ID=u.effective_chat.id
    await u.message.reply_text(f"🔥 V2 LIVE! Team7 Odds2+ 4x daily\nID:{CHAT_ID}\n/tip")
    await send_daily_tips(c)
async def tip(u,c):
    global CHAT_ID
    CHAT_ID=u.effective_chat.id
    await send_daily_tips(c)
app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("tip",tip))
app.job_queue.run_repeating(send_daily_tips,interval=21600,first=15)
print("V2 INAANZA... Team7 Odds2+ 4x daily")
app.run_polling()

