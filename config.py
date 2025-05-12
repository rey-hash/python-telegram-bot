import os

def get_bot_token():
    return os.getenv("TELEGRAM_BOT_TOKEN") or input("Enter your Telegram Bot Token: ").strip()
