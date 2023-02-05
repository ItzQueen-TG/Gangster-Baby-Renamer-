from datetime import date as date_
import datetime
import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup)
from plugins.cb_data import app


CHANNEL = os.environ.get('CHANNEL', "")
STRING = os.environ.get("STRING", "")
ADMIN = int(os.environ.get("ADMIN", 1484670284))
bot_username = os.environ.get("BOT_USERNAME","GangsterBaby_renamer_BOT")
log_channel = int(os.environ.get("LOG_CHANNEL", ""))
token = os.environ.get('TOKEN', '')
botid = token.split(':')[0]
FLOOD = 500
LAZY_PIC = os.environ.get("LAZY_PIC", "")


# Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    wish = "❤️ Good morning sweetheart ❤️"
elif 12 <= currentTime.hour < 12:
    wish = '🤍 Good afternoon my Love 🤍'
else:
    wish = '🦋 Good evening baby 🦋'

# -------------------------------

@app.on_message(filters.private)
async def pm_reply(bot, msg):
    a = await msg.reply_chat_action(enums.ChatAction.TYPING)
    await asyncio.sleep(0.4)
    b = await msg.reply_text("👀")
