from pyrogram import Client, filters

@Client.on_message(filters.command("help"))
async def help_cmd(client, message):
    help_text = '''
📖 Teleroid Commands:
/start - Welcome message
/help - This help menu
/ping - Check if bot is alive
/id - Get your Telegram ID
/location <city> - Get city coordinates
/waifu - Grab a random waifu
'''
    await message.reply_text(help_text)
  
