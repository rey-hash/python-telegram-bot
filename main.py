import telebot

bot = telebot.TeleBot("8027621381:AAGuZ-nCc_NUNm9anX3aVG_P0btg8vgc_qM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()



# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	pass

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	pass

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass

# Handles all messages for which the lambda returns True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
	pass

# Which could also be defined as:
def test_message(message):
	return message.document.mime_type == 'text/plain'

@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
	pass

# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji
@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def send_something(message):
    pass





class Middleware(BaseMiddleware):
    def __init__(self):
        self.update_types = ['message']
    def pre_process(self, message, data):
        data['foo'] = 'Hello' # just for example
        # we edited the data. now, this data is passed to handler.
        # return SkipHandler() -> this will skip handler
        # return CancelUpdate() -> this will cancel update
    def post_process(self, message, data, exception=None):
        print(data['foo'])
        if exception: # check for exception
            print(exception)
            
            
class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    # Class will check whether the user is admin or creator in group or not
    key='is_chat_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']
	
# To register filter, you need to use method add_custom_filter.
bot.add_custom_filter(IsAdmin())
	
# Now, you can use it in handler.
@bot.message_handler(is_chat_admin=True)
def admin_of_group(message):
	bot.send_message(message.chat.id, 'You are admin of this group!')



import telebot

TOKEN = '<token_string>'
tb = telebot.TeleBot(TOKEN)	#create a new Telegram Bot object

# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - interval: int (default 0) - The interval between polling requests
# - timeout: integer (default 20) - Timeout in seconds for long polling.
# - allowed_updates: List of Strings (default None) - List of update types to request 
tb.infinity_polling(interval=0, timeout=20)

# getMe
user = tb.get_me()

# setWebhook
tb.set_webhook(url="http://example.com", certificate=open('mycert.pem'))
# unset webhook
tb.remove_webhook()

# getUpdates
updates = tb.get_updates()
# or
updates = tb.get_updates(1234,100,20) #get_Updates(offset, limit, timeout):

# sendMessage
tb.send_message(chat_id, text)

# editMessageText
tb.edit_message_text(new_text, chat_id, message_id)

# forwardMessage
tb.forward_message(to_chat_id, from_chat_id, message_id)

# All send_xyz functions which can take a file as an argument, can also take a file_id instead of a file.
# sendPhoto
photo = open('/tmp/photo.png', 'rb')
tb.send_photo(chat_id, photo)
tb.send_photo(chat_id, "FILEID")

# sendAudio
audio = open('/tmp/audio.mp3', 'rb')
tb.send_audio(chat_id, audio)
tb.send_audio(chat_id, "FILEID")

## sendAudio with duration, performer and title.
tb.send_audio(CHAT_ID, file_data, 1, 'eternnoir', 'pyTelegram')

# sendVoice
voice = open('/tmp/voice.ogg', 'rb')
tb.send_voice(chat_id, voice)
tb.send_voice(chat_id, "FILEID")

# sendDocument
doc = open('/tmp/file.txt', 'rb')
tb.send_document(chat_id, doc)
tb.send_document(chat_id, "FILEID")

# sendSticker
sti = open('/tmp/sti.webp', 'rb')
tb.send_sticker(chat_id, sti)
tb.send_sticker(chat_id, "FILEID")

# sendVideo
video = open('/tmp/video.mp4', 'rb')
tb.send_video(chat_id, video)
tb.send_video(chat_id, "FILEID")

# sendVideoNote
videonote = open('/tmp/videonote.mp4', 'rb')
tb.send_video_note(chat_id, videonote)
tb.send_video_note(chat_id, "FILEID")

# sendLocation
tb.send_location(chat_id, lat, lon)

# sendChatAction
# action_string can be one of the following strings: 'typing', 'upload_photo', 'record_video', 'upload_video',
# 'record_audio', 'upload_audio', 'upload_document' or 'find_location'.
tb.send_chat_action(chat_id, action_string)

# getFile
# Downloading a file is straightforward
# Returns a File object
import requests
file_info = tb.get_file(file_id)

file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))


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



from telebot import apihelper

apihelper.API_URL = "http://localhost:4200/bot{0}/{1}"


def handle_messages(messages):
	for message in messages:
		# Do something with the message
		bot.reply_to(message, 'Hi')

bot.set_update_listener(handle_messages)
bot.infinity_polling()


import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.


from telebot import apihelper

apihelper.proxy = {'http':'http://127.0.0.1:3128'}

apihelper.proxy = {'https':'socks5://userproxy:password@proxy_address:port'}

apihelper.CUSTOM_REQUEST_SENDER = your_handler


def custom_sender(method, url, **kwargs):
    print("custom_sender. method: {}, url: {}, params: {}".format(method, url, kwargs.get("params")))
    result = util.CustomRequestResponse('{"ok":true,"result":{"message_id": 1, "date": 1, "chat": {"id": 1, "type": "private"}}}')
    return Result
    
    
apihelper.CUSTOM_REQUEST_SENDER = custom_sender
tb = TeleBot("test")
res = tb.send_message(123, "Test")





from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext



def start(update: Update, context: CallbackContext):
    """Responds when the user sends /start"""
    update.message.reply_text("Hello! Welcome to my bot.")

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




