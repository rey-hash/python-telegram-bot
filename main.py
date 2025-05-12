import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config import get_bot_token
from handlers import commands, inline

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    token = get_bot_token()
    app = ApplicationBuilder().token(token).build()

    # Command Handlers
    app.add_handler(CommandHandler("start", commands.start))
    app.add_handler(CommandHandler("help", commands.help_command))
    app.add_handler(CommandHandler("about", commands.about))
    app.add_handler(CommandHandler("echo", commands.echo_command))
    app.add_handler(CommandHandler("time", commands.time_command))
    app.add_handler(CommandHandler("id", commands.id_command))
    app.add_handler(CommandHandler("inline", inline.inline_menu))

    # Callback Query Handler for Inline Buttons
    app.add_handler(CallbackQueryHandler(inline.handle_callback))

    # Text Message Handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, commands.echo_text))

    print("Bot is running. Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
