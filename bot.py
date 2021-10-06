# (c) ffmpeg knowledge (c) @Animes_Encoded 

from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent)
from config import Config
from config import app as ffmpeg
button=[]
button.append([[InlineKeyboardButton("Help", callback_data="ihelp")]])
button.append([[InlineKeyboardButton("Guide", callback_data="iguide")]])

bbutton=[]
bbutton.append([[InlineKeyboardButton("Back", callback_data="beck")]])
# python (c) list 


@ffmpeg.on_message(filters.command(['start']))
def start(client, message):
  rep = =f"Hi {message.from_user.username} \n <b> I am one simple bot  made by @Bro_isDarkal \nPls click the below buttons to get a hint about this bot !\n\n By @Animes_Encoded.<b> \n",
  message.reply_text(
    text=rep,
    rep =f"Hi {message.from_user.username} \n <b> I am one simple bot  made by @Bro_isDarkal \nPls click the below buttons to get a hint about this bot !\n\n By @Animes_Encoded.<b> \n",
    message.reply_text(
        text=rep,
        quote=False,
      
