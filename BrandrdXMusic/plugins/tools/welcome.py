import os
from logging import getLogger

from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import filters
from pyrogram.types import (
    ChatMemberUpdated,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from BrandrdXMusic import app
import config

LOGGER = getLogger(__name__)

# ─────────────────────────────────────────────
# Safe LOG_CHANNEL_ID (NO CRASH)
# ─────────────────────────────────────────────
LOG_CHANNEL_ID = getattr(config, "LOG_CHANNEL_ID", None)

# ─────────────────────────────────────────────
# Simple in-memory welcome toggle DB
# ─────────────────────────────────────────────
class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        self.data[chat_id] = {}

    async def rm_wlcm(self, chat_id):
        self.data.pop(chat_id, None)


wlcm = WelDatabase()


class temp:
    MELCOW = {}


# ─────────────────────────────────────────────
# Image helpers
# ─────────────────────────────────────────────
def circle(pfp, size=(500, 500)):
    pfp = pfp.resize(size, Image.LANCZOS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp


def welcomepic(pic, uid):
    background = Image.open("BrandrdXMusic/assets/welcome_bg.png").convert("RGBA")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp).resize((825, 824))

    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("BrandrdXMusic/assets/font.ttf", size=90)

    draw.text((2100, 1420), f"ID : {uid}", fill=(255, 255, 255), font=font)
    background.paste(pfp, (1990, 435), pfp)

    path = f"downloads/welcome_{uid}.png"
    background.save(path)
    return path


# ─────────────────────────────────────────────
# Group member welcome
# ─────────────────────────────────────────────
@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return

    chat_id = member.chat.id
    user = member.new_chat_member.user

    try:
        pic = await app.download_media(
            user.photo.big_file_id,
            file_name=f"downloads/pp{user.id}.png",
        )
    except Exception:
        pic = "BrandrdXMusic/assets/welcome_bg.png"

    old = temp.MELCOW.get(chat_id)
    if old:
        try:
            await old.delete()
        except Exception:
            pass

    try:
        welcomeimg = welcomepic(pic, user.id)

        temp.MELCOW[chat_id] = await app.send_photo(
            chat_id,
            photo=welcomeimg,
            caption=(
                f"✨ **WELCOME TO {member.chat.title}** ✨\n"
                f"━━━━━━━━━━━━━━━━━━\n"
                f"👤 **Name** : {user.mention}\n"
                f"🆔 **ID** : `{user.id}`\n"
                f"🔗 **Username** : @{user.username}\n\n"
                f"⚡ **Powered By : EVID CORE**\n"
                f"👑 **Owner : @xxbga**\n"
                f"━━━━━━━━━━━━━━━━━━"
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "➕ Add EvidXMusic",
                            url=f"https://t.me/{app.username}?startgroup=true",
                        )
                    ]
                ]
            ),
        )
    except Exception as e:
        LOGGER.error(f"Welcome error: {e}")

    for f in (
        f"downloads/welcome_{user.id}.png",
        f"downloads/pp{user.id}.png",
    ):
        try:
            os.remove(f)
        except Exception:
            pass


# ─────────────────────────────────────────────
# Bot added to new group → optional log
# ─────────────────────────────────────────────
@app.on_message(filters.new_chat_members & filters.group, group=-1)
async def bot_wel(_, message: Message):
    if not LOG_CHANNEL_ID:
        return

    for u in message.new_chat_members:
        if u.id == app.me.id:
            try:
                await app.send_message(
                    LOG_CHANNEL_ID,
                    (
                        "➕ **NEW GROUP ADDED**\n"
                        "━━━━━━━━━━━━━━━━━━\n"
                        f"📛 **Name** : {message.chat.title}\n"
                        f"🆔 **ID** : `{message.chat.id}`\n"
                        f"🔗 **Username** : @{message.chat.username}\n\n"
                        f"⚡ **Bot** : {app.mention}\n"
                        f"👑 **Owner** : @xxbga\n"
                        "━━━━━━━━━━━━━━━━━━"
                    ),
                )
            except Exception as e:
                LOGGER.error(f"Log send failed: {e}")
