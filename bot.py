import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8672116331:AAGBn087ibZkEdTO034efQNPzQ3pinfw6m0")

app = Flask(__name__)

application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum 👋\n\nHokim ariza botiga xush kelibsiz!\n\nAriza yuborish uchun yozishni boshlang."
    )

application.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "ok"

@app.route("/")
def home():
    return "Bot ishlayapti 🚀"

if __name__ == "__main__":
    application.initialize()
    application.start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
