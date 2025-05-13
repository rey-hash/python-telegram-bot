from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

async def inline_button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"You clicked: {query.data}")

def register_inline_handlers(app):
    app.add_handler(CallbackQueryHandler(inline_button_callback))