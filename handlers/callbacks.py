
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton


from telegram.ext import ContextTypes, CallbackQueryHandler


async def inline_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'say_hello':
        await query.message.reply_text(
            f"Hello, {query.from_user.first_name}!",
            reply_to_message_id=query.message.message_id
        )

    elif query.data == 'user_info':
        user = query.from_user
        user_info = (
            f"User Info:\n"
            f"Name: {user.full_name}\n"
            f"Username: @{user.username if user.username else 'N/A'}\n"
            f"ID: {user.id}"
        )
        await query.message.reply_text(
            user_info,
            reply_to_message_id=query.message.message_id
        )



async def inline_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"You clicked: {query.data}")

def register_inline_handlers(app):
    app.add_handler(CallbackQueryHandler(inline_button_callback))