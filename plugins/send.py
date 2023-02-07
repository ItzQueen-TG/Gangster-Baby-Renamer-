import re
import os 
import math
import time
import humanize
import asyncio

from pyrogram import Client, filters
from info import ADMINS, CAPTION, temp
from pyrogram.types import *
from pyrogram.errors import FloodWait

@Client.on_message(filters.private & filters.command("set") & filters.user(ADMINS))                            
async def set_tumb(bot, msg):
    replied = msg.reply_to_message
    if not replied:
        await msg.reply("use this command with Reply to a photo")
        return
    if not msg.reply_to_message.photo:
       await msg.reply("Oops !! this is Not a photo")
       return
    Tumb = msg.reply_to_message.photo.file_id
    temp.THUMBNAIL = Tumb
    return await msg.reply(f"Temporary Thumbnail saved✅️ \nDo You want permanent thumbnail. \n\n`{Tumb}` \n\n👆👆 please add this id to your server enviro with key=`THUMBNAIL`")            



@Client.on_message(filters.private & (filters.document | filters.video))
async def send_file(bot, msg):
    media = msg.document or msg.audio or msg.video
    og_media = getattr(msg, msg.media.value)
    filename = og_media.file_name
    new_name = filename
    sts = await bot.send_message(chat_id=msg.from_user.id, text=f"Trying to Download 📩\n\n`{new_name}`")
    c_time = time.time()
    download = new_name
    download = await msg.download(file_name=new_name, progress=progress_message, progress_args=(f"`{new_name}`", sts, c_time))
    filesize = humanbytes(og_media.file_size)
    if CAPTION:
        try:
            cap = CAPTION.format(file_name=new_name, file_size=filesize)
        except Exception as e:            
            await sts.edit(text=f"Your caption Error unexpected keyword ●> ({e})")
            return
    else:
        cap = f"`{new_name}`"
    raw_thumbnail = temp.THUMBNAIL 
    thumb_tg = og_media.file_size
    if raw_thumbnail:
        thumb_tg = await bot.download_media(raw_thumbnail)
    else:
        thumb_tg = await bot.download_media(og_media.thumbs[0].file_id)
    await sts.edit(f"Trying to Uploading\n`{new_name}`")
    c_time = time.time()
    try:
        await bot.send_document(msg.from_user.id, document=downloaded, thumb=thumb_tg, caption=cap, progress=progress_message, progress_args=(f"Uploading 📤\n\n`{new_name}`", sts, c_time))
    except Exception as e:  
        await msg.copy(chat_id=msg.from_user.id, caption = cap)
        await sts.delete()
        return               
    try:
        os.remove(downloaded)
        os.remove(thumb_tg)
    except:
        pass
    await sts.delete()
