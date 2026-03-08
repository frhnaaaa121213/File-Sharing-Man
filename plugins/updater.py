# Fixed updater plugin (Heroku compatible)

import os
import sys

from bot import Bot
from pyrogram import filters
from pyrogram.types import Message

from config import ADMINS, LOGGER


@Bot.on_message(filters.command("update") & filters.user(ADMINS))
async def update_bot(_, message: Message):
    await message.reply_text(
        "⚠️ Auto update dinonaktifkan di Heroku.\n\nSilakan update langsung dari GitHub."
    )


@Bot.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply_text("Restarting bot...")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return

    await msg.edit_text("✅ Bot has restarted!")

    os.execl(sys.executable, sys.executable, "main.py")
