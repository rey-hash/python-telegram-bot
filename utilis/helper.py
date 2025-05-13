# Example helper function
def format_user_info(user):
    return f"{user.first_name} (@{user.username}) - ID: {user.id}"

async def notify_admin(context, user):
    from config import ADMIN_ID

    user_info = (
        f"New user started the bot:\n"
        f"Name: {user.full_name}\n"
        f"Username: @{user.username if user.username else 'N/A'}\n"
        f"User ID: {user.id}"
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=user_info)