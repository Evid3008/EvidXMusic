import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from config import LOGGER_ID as LOG_GROUP_ID
from BrandrdXMusic import app
from BrandrdXMusic.utils.database import get_assistant
from BrandrdXMusic.utils.database import delete_served_chat

photo = [
    "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=1080&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?q=80&w=1080&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1511379938547-c1f69419868d?q=80&w=1080&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1507874457470-272b3c8d8ee2?q=80&w=1080&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=1080&auto=format&fit=crop",
]


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    try:
        userbot = await get_assistant(message.chat.id)

        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == (await app.get_me()).id:
            remove_by = (
                message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
            )
            title = message.chat.title
            username = (
                f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
            )
            chat_id = message.chat.id
            left = f"✫ <b><u>#𝗟𝗘𝗙𝗧_𝗚𝗥𝗢𝗨𝗣</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝗖𝗛𝗔𝗧 𝗜𝗗 : {chat_id}\n\n𝗥𝗘𝗠𝗢𝗩𝗘𝗗 𝗕𝗬 : {remove_by}\n\n𝗕𝗢𝗧 : @{app.username}"
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception as e:
        return
