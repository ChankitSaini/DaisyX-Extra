# Made by @Kraken_The_BadASS for @HellBot_Official

from telethon import events
from asyncio import sleep
import os, sys, random, re
from DaisyX.utils import admin_cmd
from DaisyX import bot

# By Team DC 

@borg.on(admin_cmd(pattern="wspr ?(.*)"))
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()
    
