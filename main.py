from flask import Flask
from threading import Thread
import telebot
from telebot import types
import os

BOT_TOKEN = os.environ.get("8027621381:AAGuZ-nCc_NUNm9anX3aVG_P0btg8vgc_qM")
bot = telebot.TeleBot(BOT_TOKEN)

# Flask Web Server for UptimeRobot
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

# Telegram Bot Handlers
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Use /menu for options or /inline for inline menu.")

@bot.message_handler(commands=['menu'])
def send_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        types.KeyboardButton('Option A'),
        types.KeyboardButton('Option B'),
        types.KeyboardButton('Option C')
    )
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(commands=['inline'])
def inline_menu(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Google", url="https://google.com"),
        types.InlineKeyboardButton("Option 1", callback_data='1'),
        types.InlineKeyboardButton("Option 2", callback_data='2')
    )
    bot.send_message(message.chat.id, "Choose an inline option:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    bot.answer_callback_query(call.id, f"You selected: {call.data}")

def run_bot():
    bot.infinity_polling()

# Run both Flask and Bot in parallel
if __name__ == "__main__":
    Thread(target=run_web).start()
    run_bot()