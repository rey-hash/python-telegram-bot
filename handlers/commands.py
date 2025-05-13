




from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
from utils.helpers import notify_admin


from telegram import InlineKeyboardMarkup, InlineKeyboardButton





from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Say Hello", callback_data='say_hello')],
        [InlineKeyboardButton("Get User Info", callback_data='user_info')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text("Hello! Welcome to the bot.")
    await notify_admin(context, user)  # Notify admin when user starts
# /start command
    await update.message.reply_text("Hello! I am your Echo Bot.\nSend me any text or use /help to see commands.")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/about - About this bot\n"
        "/echo <text> - Echo your text\n"
        "/time - Server time\n"
        "/id - Your Telegram ID\n"
        "/info - Your profile info\n"
        "/chatinfo - Current chat info\n"
        "/ping - Test bot is alive\n"
        "/reverse <text> - Reverse your text\n"
        "/uppercase <text> - Make text UPPERCASE\n"
        "/weather - Dummy weather info"
    )
    await update.message.reply_text(help_text)

# /about command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = (
        "I am a simple Echo Bot built with python-telegram-bot.\n"
        "I can echo messages, reply to commands, and do simple tricks."
    )
    await update.message.reply_text(about_text)

# /echo command
async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        text_to_echo = ' '.join(context.args)
        await update.message.reply_text(text_to_echo)
    else:
        await update.message.reply_text("Usage: /echo <your text>")

# /time command
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(f"Current server time: {now}")

# /id command
async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(f"Your Telegram ID: {user_id}")

# /info command
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    info_text = (
        f"Username: @{user.username}\n"
        f"First Name: {user.first_name}\n"
        f"Last Name: {user.last_name or 'N/A'}\n"
        f"User ID: {user.id}"
    )
    await update.message.reply_text(info_text)

# /chatinfo command
async def chatinfo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    chat_text = (
        f"Chat ID: {chat.id}\n"
        f"Type: {chat.type}\n"
        f"Title: {chat.title or 'Private Chat'}"
    )
    await update.message.reply_text(chat_text)

# /ping command
async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pong!")

# /reverse command
async def reverse_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        reversed_text = ' '.join(context.args)[::-1]
        await update.message.reply_text(reversed_text)
    else:
        await update.message.reply_text("Usage: /reverse <your text>")

# /uppercase command
async def uppercase_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        upper_text = ' '.join(context.args).upper()
        await update.message.reply_text(upper_text)
    else:
        await update.message.reply_text("Usage: /uppercase <your text>")

# /weather command (dummy)
async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Weather API not connected yet. (Demo function.)")