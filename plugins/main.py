import pyrogram, asyncio, random, time, os
from pyrogram import Client, filters, enums
from pyrogram.types import *
from helper.database import add_user
from variables import PICS
from helper.text import txt

@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    await add_user(bot, message)    
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/Pro_CoderZ"),
        InlineKeyboardButton("ᴜᴩᴅᴀᴛᴇꜱ", url="https://t.me/ProCoderZBots")
        ],[            
        InlineKeyboardButton("Mᴏʀᴇ Bᴏᴛs", url="https://t.me/ProCoderZBots/12")
    ]])
        
    await message.reply_text(text=txt.STAT.format(message.from_user.mention), reply_markup=button, disable_web_page_preview=True)
        
                                              
@Client.on_message(filters.command(["zhssd", "zjso"]))
async def media_info(bot, m): 
    message = m
    ff = m.from_user
    md = m.reply_to_message
    if md:
       try:
          if md.photo:
              await m.reply_text(text=f"**your photo id is **\n\n`{md.photo.file_id}`") 
          if md.sticker:
              await m.reply_text(text=f"**your sticker id is **\n\n`{md.sticker.file_id}`")
          if md.video:
              await m.reply_text(text=f"**your video id is **\n\n`{md.video.file_id}`")
          if md.document:
              await m.reply_text(text=f"**your document id is **\n\n`{md.document.file_id}`")
          if md.audio:
              await m.reply_text(text=f"**your audio id is **\n\n`{md.audio.file_id}`")
          if md.text:
              await m.reply_text("**hey man please reply with ( photo, video, sticker, documents, etc...) Only media **")  
          else:
              await m.reply_text("[404] Error..🤖")                                                                                      
       except Exception as e:
          print(e)
          await m.reply_text(f"[404] Error {e}")
                                        
    if not md:
        buttons = [[
            InlineKeyboardButton("✨️ Support", url="https://t.me/ProCoderZBots"),
            InlineKeyboardButton("📢 Updates", url="https://t.me/ProCoderZBots")
        ]]       
        mkn = await m.reply("please wait....")
        if ff.photo:
           user_dp = await bot.download_media(message=ff.photo.big_file_id)
           await m.reply_photo(
               photo=user_dp,
               caption=txt.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username),
               reply_markup=InlineKeyboardMarkup(buttons),
               quote=True,
               parse_mode=enums.ParseMode.HTML,
               disable_notification=True
           )          
           os.remove(user_dp)
           await mkn.delete()
        else:  
           await m.reply_text(
               text=txt.INFO_TXT.format(id=ff.id, dc=ff.dc_id, n=ff.first_name, u=ff.username),
               reply_markup=InlineKeyboardMarkup(buttons),
               quote=True,
               parse_mode=enums.ParseMode.HTML,
               disable_notification=True
           )

