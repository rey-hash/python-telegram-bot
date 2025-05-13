

import os


ADMIN_ID = 6557975040  # Replace with your Telegram user ID

def get_bot_token():
    # Get token from environment variable or ask user
    token = os.getenv("TELEGRAM_BOT_TOKEN") or input("Enter your Telegram Bot Token: ").strip()
    if not token:
        raise ValueError("Bot token is required.")
    return token