async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(f"Your Telegram ID is: {user_id}") 


from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from datetime import datetime
import time

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am your modular bot. Use /help to see commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Commands:\n"
        "/start - Start bot\n"
        "/help - Help menu\n"
        "/about - About this bot\n"
        "/echo <text> - Echo text\n"
        "/time - Server time\n"
        "/status - Bot status\n"
        "/userinfo - Your info\n"
        "/chatinfo - Chat info\n"
        "/ping - Latency"
    )
    await update.message.reply_text(text)

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Modular Telegram Bot using python-telegram-bot 20.x")

async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await update.message.reply_text(' '.join(context.args))
    else:
        await update.message.reply_text("Usage: /echo <text>")

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(f"Current server time: {now}")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is up and running!")

async def userinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"User ID: {user.id}\n"
        f"Username: @{user.username}\n"
        f"First Name: {user.first_name}\n"
        f"Language: {user.language_code}"
    )
    await update.message.reply_text(text)

async def chatinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    text = (
        f"Chat ID: {chat.id}\n"
        f"Type: {chat.type}\n"
        f"Title: {chat.title or 'Private'}"
    )
    await update.message.reply_text(text)

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start = time.time()
    msg = await update.message.reply_text("Pinging...")
    latency = (time.time() - start) * 1000
    await msg.edit_text(f"Pong! {latency:.2f} ms")

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("echo", echo_command))
    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("userinfo", userinfo))
    app.add_handler(CommandHandler("chatinfo", chatinfo))
    app.add_handler(CommandHandler("ping", ping))