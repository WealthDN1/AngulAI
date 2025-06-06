cd telegram-gpt-bot
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set environment variables (temporarily for testing)
export OPENAI_API_KEY="your-key-here"
export TELEGRAM_BOT_TOKEN="your-telegram-token"

# Run the bot
python bot.py
