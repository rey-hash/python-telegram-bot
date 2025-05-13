import logging
import os
from telegram.ext import ApplicationBuilder
from handlers import commands, messages, callbacks  # Import callbacks added


from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, filters


# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Get token
bot_token = os.getenv("TELEGRAM_BOT_TOKEN") or input("Please enter your bot token: ").strip()
if not bot_token:
    print("Error: Bot token cannot be empty. Exiting.")
    exit(1)

# Build app
app = ApplicationBuilder().token(bot_token).build()

# Command Handlers
app.add_handler(CommandHandler("start", commands.start))
app.add_handler(CommandHandler("help", commands.help_command))
app.add_handler(CommandHandler("about", commands.about))
app.add_handler(CommandHandler("echo", commands.echo_command))
app.add_handler(CommandHandler("time", commands.time_command))
app.add_handler(CommandHandler("id", commands.id_command))
app.add_handler(CommandHandler("info", commands.info_command))
app.add_handler(CommandHandler("chatinfo", commands.chatinfo_command))
app.add_handler(CommandHandler("ping", commands.ping_command))
app.add_handler(CommandHandler("reverse", commands.reverse_command))
app.add_handler(CommandHandler("uppercase", commands.uppercase_command))
app.add_handler(CommandHandler("weather", commands.weather_command))

app.add_handler(CommandHandler("menu", commands.menu_command))  # Inline menu command


# Inline Button Handlers
callbacks.register_inline_handlers(app)

# Register callback for inline buttons
app.add_handler(CallbackQueryHandler(callbacks.inline_button_callback))



# Echo text messages
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messages.echo))

# Start Bot
print("Bot is running. Press Ctrl+C to stop.")
app.run_polling()






