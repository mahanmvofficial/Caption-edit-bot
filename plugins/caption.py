# @TheStyleKing

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

mv_buttons = [[
        InlineKeyboardButton('💢 Share Our Group 💢', url='http://t.me/share/url?url=Join%20@KannadaMVRequest%20To%20Request%20Kannada%20Movies')
    ],[
        InlineKeyboardButton('💢 Join Our Official Channel 💢', url="t.me/MahanCreations")
    ]] 
@Client.on_message(filters.document & filters.channel)
async def caption(client, message: Message):
    await message.edit("Nice to meet you Here 💞\n✯ ━━━━━━ ✧ ━━━━━━━ ✯\nShare Our Group to friend's.\n✯ ━━━━━━ ✧ ━━━━━━━ ✯\n@KannadaMVRequest",
          reply_markup=InlineKeyboardMarkup(mv_buttons))
