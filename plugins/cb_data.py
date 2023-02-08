from helper.progress import progress_for_pyrogram, TimeFormatter

from pyrogram import Client, filters, enums
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.database import *
import os
import asyncio
import random
from PIL import Image
import time
from datetime import timedelta
from helper.ffmpeg import take_screen_shot, fix_thumb
from helper.progress import humanbytes
from helper.set import escape_invalid_curly_brackets
import os

logg_channel = int(os.environ.get("LOG_CHNNEL", "-1001479558698"))

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "")

ADMIN = os.environ.get("ADMIN", "")

app = Client("test", api_id=API_ID, api_hash=API_HASH, session_string=STRING)


@app.on_message(filters.chat(logg_channel))
async def rename_file(bot, msg):
    await msg.reply_text("<code>No matter what midnight you ask, you will get the movie, collection of movies in most languages ​​of the world.. ❤️\n\n • Join the channel and get the bot link\n\n • Left from the current group and join in the below mentioned channel\n\n👇 CHANNEL LINK 👇</code>\n\n   @Vysakh_XD\n   @Vysakh_XD\n   @Vysakh_XD\n   @Vysakh_XD\n   @Vysakh_XD")

@app.on_message(filters.private)
async def pm_reply(bot, msg):
    a = await msg.reply_chat_action(enums.ChatAction.TYPING)
    await asyncio.sleep(0.4)
    b = await msg.reply_text("hy👀")
