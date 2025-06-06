import logging
import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Load API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Set up logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm a ChatGPT bot. Just send me any message and I'll respond!")

# Message handler
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        # Call OpenAI's Chat API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" if you prefer
            messages=[{"role": "user", "content": user_message}],
        )
        reply = response["choices"][0]["message"]["content"]
        await update.message.reply_text(reply)

    except Exception as e:
        await update.message.reply_text(f"⚠ Error: {str(e)}")

# Main entry point
if _name_ == "_main_":
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()
