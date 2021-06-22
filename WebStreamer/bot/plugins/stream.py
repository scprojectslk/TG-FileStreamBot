# This file is a part of TG-FileStreamBot
# Coding : SC Projects LK [@SCProjectsLK]

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio), group=4)
async def media_receive_handler(_, m: Message):
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = Var.URL + str(log_msg.message_id)
    await m.reply_text(
        text="`{}`".format(stream_link),
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Open', url=stream_link)]])
    )
