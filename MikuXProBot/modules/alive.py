import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from MikuXProBot.events import register
from MikuXProBot import telethn as borg, OWNER_ID, OWNER_NAME
from MikuXProBot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/4476fd80a859163aba1e0.jpg"
file2 = "https://telegra.ph/file/16b5c19b00890b7efd984.jpg"
file3 = "https://telegra.ph/file/5bd4876b8de01ee2a0361.jpg"
file4 = "https://telegra.ph/file/262cd3ee5fff9e28682d7.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    Miku = f"♡ **ʜᴇʏ [{yes.sender.first_name}](tg://user?id={yes.sender.id}), ɪ ᴀᴍ ᴛʀᴏᴊᴀɴs ʀᴏʙᴏᴛ **\n\n"
    Miku += f"♡ **Mʏ  Uᴘᴛɪᴍᴇ** ~♪ `{uptime}`\n\n"
    Miku += f"♡ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ** ~♪ `{version.__version__}`\n\n"
    Miku += f"♡ **Pʏᴛʜᴏɴ  Bᴏᴛ Vᴇʀsɪᴏɴ** ~♪ `{telegram.__version__}`\n\n"
    Miku += f"♡ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ** ~♪ `{pyro}`\n\n"
    Miku += f"♡ **Mʏ Mᴀsᴛᴇʀ** ~♪ [{OWNER_NAME}](tg://user?id={OWNER_ID})\n\n"
    Miku += f"Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ Iɴ {yes.chat.title}"
    BUTTON = [[Button.url("Support Chat", "https://t.me/TROJANS_x_SUPPORT"), Button.url("Updates Channel", "https://t.me/TROJANS_x_UPDATES")]]
    on = await borg.send_file(yes.chat_id, file=file2,caption=Miku, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file3, buttons=BUTTON) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file4, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file2, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4, buttons=BUTTON)

@register(pattern=("/repo"))
async def repo(event):
    Miku = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), Click The Button Below To Get My Repo**\n\n"
    BUTTON = [[Button.url("[► Support ◄]", "https://t.me/TROJANS_x_SUPPORT"), Button.url("[► Repo ◄]", "")]]
    await borg.send_file(event.chat_id, file="https://telegra.ph/file/262cd3ee5fff9e28682d7.jpg", caption=Miku, buttons=BUTTON)
