from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your Echo Bot.\nUse /help to see available commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/about - Info about this bot\n"
        "/echo <text> - I will repeat your text\n"
        "/time - Show current server time\n"
        "/id - Show your Telegram user ID"
    )
    await update.message.reply_text(help_text)

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = (
        "I am a simple Echo Bot built with python-telegram-bot.\n"
        "Made with async functions!"
    )
    await update.message.reply_text(about_text)

async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        text_to_echo = ' '.join(context.args)
        await update.message.reply_text(text_to_echo)
    else:
        await update.message.reply_text("Usage: /echo <your text>")

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(f"Current server time: {now}")

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(f"Your Telegram ID is: {user_id}")
