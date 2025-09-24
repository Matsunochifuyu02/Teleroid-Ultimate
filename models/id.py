from pyrogram import Client, filters

@Client.on_message(filters.command("id"))
async def id_cmd(client, message):
    user = message.from_user
    await message.reply_text(f"👤 ID: {user.id}\n📝 Name: {user.first_name}")
