from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def register_handlers(app):
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))