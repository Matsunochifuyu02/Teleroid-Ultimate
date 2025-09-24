from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("👋 Welcome to Teleroid v1.0!
Type /help to see commands.")
