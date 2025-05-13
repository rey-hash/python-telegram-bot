import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import get_bot_token
from handlers import commands, from handlers import messages
from handlers.inline import register_inline_handlers

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Echo any non-command text
async def echo(update, context):
    await update.message.reply_text(update.message.text)

def main():
    token = get_bot_token()
    app = ApplicationBuilder().token(token).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", commands.start))
    app.add_handler(CommandHandler("help", commands.help_command))
    app.add_handler(CommandHandler("about", commands.about))
    app.add_handler(CommandHandler("echo", commands.echo_command))
    app.add_handler(CommandHandler("time", commands.time_command))
    app.add_handler(CommandHandler("id", commands.id_command))

    # Register inline buttons handlers
    register_inline_handlers(app)

    # Echo normal text
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start polling
    print("Bot is running. Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
