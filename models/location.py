from pyrogram import Client, filters
import requests

@Client.on_message(filters.command("location"))
async def location_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /location <city>")
    city = ' '.join(message.command[1:])
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    data = requests.get(url).json()
    if "results" not in data:
        return await message.reply_text("Location not found")
    result = data["results"][0]
    reply = f"📍 {result['name']}, {result['country']}\n🌐 Lat: {result['latitude']} | Lon: {result['longitude']}"
    await message.reply_text(reply)
