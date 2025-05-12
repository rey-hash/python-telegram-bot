import os

def get_bot_token():
    # Get token from environment variable or ask user
    token = os.getenv("TELEGRAM_BOT_TOKEN") or input("Enter your Telegram Bot Token: ").strip()
    if not token:
        raise ValueError("Bot token is required.")
    return token