from helper.progress import progress_for_pyrogram, TimeFormatter

from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.database import *
import os
import random
from PIL import Image
import time
from datetime import timedelta
from helper.ffmpeg import take_screen_shot, fix_thumb
from helper.progress import humanbytes
from helper.set import escape_invalid_curly_brackets
import os

log_channel = int(os.environ.get("LOG_CHANNEL", ""))

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "")

ADMIN = os.environ.get("ADMIN", "")

app = Client("test", api_id=API_ID, api_hash=API_HASH, session_string=STRING)


@Client.on_callback_query(filters.regex('cancel'))
async def cancel(bot, update):
    try:
        await update.message.delete()
    except:
        return

@Client.on_message(filters.private & (filters.document | filters.video))
async def rename_file(bot, msg):
    await app.send_message(int(msg.from_user.id), "sending")

