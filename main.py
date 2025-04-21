import telebot
from telebot import types

BOT_TOKEN = "8027621381:AAGuZ-nCc_NUNm9anX3aVG_P0btg8vgc_qM"  # Replace with your actual token
bot = telebot.TeleBot(BOT_TOKEN)

# 1. Start & Help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Use /menu for options or /inline for inline menu.")

# 2. Reply Keyboard
@bot.message_handler(commands=['menu'])
def send_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Option A')
    itembtn2 = types.KeyboardButton('Option B')
    itembtn3 = types.KeyboardButton('Option C')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

# 3. Inline Keyboard
@bot.message_handler(commands=['inline'])
def inline_menu(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Google", url="https://google.com")
    btn2 = types.InlineKeyboardButton("Option 1", callback_data='1')
    btn3 = types.InlineKeyboardButton("Option 2", callback_data='2')
    markup.add(btn1)
    markup.add(btn2, btn3)
    bot.send_message(message.chat.id, "Choose an inline option:", reply_markup=markup)

# Handle inline button responses
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    bot.answer_callback_query(call.id, f"You selected: {call.data}")

# Start polling
bot.infinity_polling()