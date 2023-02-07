import re
import os 
import math
import time
import humanize
import asyncio

from PIL import Image
from pyrogram import Client, filters
from info import ADMINS, CAPTION, temp
from pyrogram.types import *
from pyrogram.errors import FloodWait


CHANNEL = int(os.environ.get("CHANNEL", "-1001837941527"))

@Client.on_message(filters.chat(CHANNEL) & (filters.document | filters.video))
async def rename_file(bot, msg):
    media = msg.document or msg.audio or msg.video
    og_media = getattr(msg, msg.media.value)
    filename = og_media.file_name
    new_name = filename
    value = 30000000
    if value > media.file_size:
        try:
            await msg.delete()
        except:
            pass
