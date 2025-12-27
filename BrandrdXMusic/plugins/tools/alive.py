import asyncio

from BrandrdXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo="https://images.unsplash.com/photo-1510519138101-570d1dca3d66?q=80&w=1080&auto=format&fit=crop",
        caption=(
            f"❤️ ʜᴇʏ {message.from_user.mention}\n\n"
            f"🔮 ɪ ᴀᴍ **{MUSIC_BOT_NAME}**\n\n"
            f"✨ ɪ ᴀᴍ ᴀ ғᴀsᴛ ᴀɴᴅ ᴘᴏᴡᴇʀғᴜʟ "
            f"ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ "
            f"sᴍᴏᴏᴛʜ ᴘᴇʀғᴏʀᴍᴀɴᴄᴇ.\n\n"
            f"💫 ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴏʀ sᴜᴘᴘᴏʀᴛ, "
            f"ʏᴏᴜ ᴄᴀɴ ᴊᴏɪɴ ᴛʜᴇ ᴄᴏʀᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ 🤍\n\n"
            f"━━━━━━━━━━━━━━━━━━❄"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text="☆ ᴄᴏʀᴇ 💗 ", url=f"https://t.me/xxbga"
            ),
            InlineKeyboardButton(
                text="☆ ꜱᴜᴘᴘᴏʀᴛ 💗", url=f"https://t.me/iq4us"
            ),
        ],
                [
            InlineKeyboardButton(
                text="☆ ᴄʜᴀɴɴᴇʟ💗", url=f"https://t.me/@devparadoxprotocol"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
