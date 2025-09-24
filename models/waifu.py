from pyrogram import Client, filters
import requests

@Client.on_message(filters.command("waifu"))
async def waifu_cmd(client, message):
    try:
        data = requests.get("https://api.waifu.pics/sfw/waifu").json()
        await message.reply_photo(photo=data['url'], caption="Here's your waifu!")
    except Exception as e:
        await message.reply_text(f"Error: {e}")
