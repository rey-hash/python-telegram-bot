import telebot

bot = telebot.TeleBot("8027621381:AAGuZ-nCc_NUNm9anX3aVG_P0btg8vgc_qM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)












from telebot import types

# Using the ReplyKeyboardMarkup class
# It's constructor can take the following optional arguments:
# - resize_keyboard: True/False (default False)
# - one_time_keyboard: True/False (default False)
# - selective: True/False (default False)
# - row_width: integer (default 3)
# row_width is used in combination with the add() function.
# It defines how many buttons are fit on each row before continuing on the next row.
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
itembtn2 = types.KeyboardButton('v')
itembtn3 = types.KeyboardButton('d')
markup.add(itembtn1, itembtn2, itembtn3)
tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)

# or add KeyboardButton one row at a time:
markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('a')
itembtnv = types.KeyboardButton('v')
itembtnc = types.KeyboardButton('c')
itembtnd = types.KeyboardButton('d')
itembtne = types.KeyboardButton('e')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)
tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)



# ReplyKeyboardRemove: hides a previously sent ReplyKeyboardMarkup
# Takes an optional selective argument (True/False, default False)
markup = types.ReplyKeyboardRemove(selective=False)
tb.send_message(chat_id, message, reply_markup=markup)


# ForceReply: forces a user to reply to a message
# Takes an optional selective argument (True/False, default False)
markup = types.ForceReply(selective=False)
tb.send_message(chat_id, "Send me another word:", reply_markup=markup)





def handle_messages(messages):
	for message in messages:
		# Do something with the message
		bot.reply_to(message, 'Hi')

bot.set_update_listener(handle_messages)
bot.infinity_polling()






from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext




def help_command(update: Update, context: CallbackContext):
    """Provides a help message"""
    update.message.reply_text("I can do the following:\n/start - Start the bot\n/help - Get help")

def about(update: Update, context: CallbackContext):
    """Provides information about the bot"""
    update.message.reply_text("This bot is created using python-telegram-bot.")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

# Adding command handlers
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler("about", about))

updater.start_polling()
updater.idle()





from telegram.ext import MessageHandler, Filters

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))





def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry, I didn't understand that command.")

dp.add_handler(MessageHandler(Filters.command, unknown))






from telegram import ReplyKeyboardMarkup

def menu(update: Update, context: CallbackContext):
    keyboard = [['Option 1', 'Option 2'], ['Option 3']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    update.message.reply_text("Choose an option:", reply_markup=reply_markup)

dp.add_handler(CommandHandler("menu", menu))





from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def inline_menu(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Google", url="https://google.com")],
                [InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose:", reply_markup=reply_markup)

dp.add_handler(CommandHandler("inline", inline_menu))





def get_id(update: Update, context: CallbackContext):
    update.message.reply_text(f"Your Telegram ID: {update.message.from_user.id}")

dp.add_handler(CommandHandler("id", get_id))


ADMIN_ID = 959683383979 # Replace with your Telegram ID

def admin_only(update: Update, context: CallbackContext):
    if update.message.from_user.id == ADMIN_ID:
        update.message.reply_text("Welcome, admin!")
    else:
        update.message.reply_text("You are not authorized to use this command.")

dp.add_handler(CommandHandler("admin", admin_only))





import random

memes = [
    "https://example.com/meme1.jpg",
    "https://example.com/meme2.jpg",
    "https://example.com/meme3.jpg"
]

def meme(update: Update, context: CallbackContext):
    update.message.reply_photo(random.choice(memes))

dp.add_handler(CommandHandler("meme", meme))




import random

def random_number(update: Update, context: CallbackContext):
    number = random.randint(1, 100)
    update.message.reply_text(f"Your random number is: {number}")

dp.add_handler(CommandHandler("random", random_number))







import requests

def weather(update: Update, context: CallbackContext):
    city = "New York"  # You can modify this or take user input
    api_url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
    
    response = requests.get(api_url).json()
    temp = response['current']['temp_c']
    
    update.message.reply_text(f"The current temperature in {city} is {temp}°C.")

dp.add_handler(CommandHandler("weather", weather))




import sys

def stop(update: Update, context: CallbackContext):
    if update.message.from_user.id == ADMIN_ID:
        update.message.reply_text("Shutting down...")
        sys.exit()
    else:
        update.message.reply_text("Only the admin can stop the bot.")

dp.add_handler(CommandHandler("stop", stop))


bot.infinity_polling()

