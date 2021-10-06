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
    quote=False,
    reply_markup=InlineKeyboardMarkup(button))

@ffmpeg.on_callback_query()
async def callback_handlers(_, event: CallbackQuery):
    if "ihelp" in event.data:
       await event.message.edit(
           message.chat.id,
           text="Checkout The Available Commands Here \n\n Do Follow @Animes_Encoded\n\n If You Find This Bot Usefull❤️",
           reply_markup=InlineKeyboardMarkup(bbutton))
    elif "iguide" in event.data:
       await event.message.edit(
         message.chat.id,
         text="Right now the bot can only compress MKV formated files and the file must be Telegram Video or Telegram Document type",
         reply_markup=InlineKeyboardMarkup(bbutton))
    elif "beck" in event.data:
       await event.message.edit(
          message.chat.id,
          text="Hi \nIam next generation video encoder bot!\n\nUpdates will come soon\n\nnMaintained by • @Animes_Encoded",
          reply_markup=InlineKeyboardMarkup(button))
        
          
       
          
# run the application        
bot.run()
      
