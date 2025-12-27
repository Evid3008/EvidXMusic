import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from BrandrdXMusic import app
from config import LOG_CHANNEL_ID

LOGGER = getLogger(__name__)

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
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()


class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None


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


def welcomepic(pic, user, chatname, uid, uname):
    background = Image.open("BrandrdXMusic/assets/welcome_bg.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp).resize((825, 824))

    draw = ImageDraw.Draw(background)
    font_big = ImageFont.truetype("BrandrdXMusic/assets/font.ttf", size=110)
    font_small = ImageFont.truetype("BrandrdXMusic/assets/font.ttf", size=60)

    draw.text((2100, 1420), f"ID: {uid}", fill=(255, 255, 255), font=font_big)
    background.paste(pfp, (1990, 435), pfp)

    path = f"downloads/welcome_{uid}.png"
    background.save(path)
    return path


# ─────────────────────────────────────────────
# Group member welcome
# ─────────────────────────────────────────────
@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return

    user = member.new_chat_member.user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except:
        pic = "BrandrdXMusic/assets/welcome_bg.png"

    if temp.MELCOW.get(f"welcome-{chat_id}"):
        try:
            await temp.MELCOW[f"welcome-{chat_id}"].delete()
        except:
            pass

    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )

        temp.MELCOW[f"welcome-{chat_id}"] = await app.send_photo(
            chat_id,
            photo=welcomeimg,
            caption=f"""
✨ **WELCOME TO {member.chat.title}** ✨
━━━━━━━━━━━━━━━━━━
👤 **Name** : {user.mention}
🆔 **ID** : `{user.id}`
🔗 **Username** : @{user.username}

⚡ **Powered By : EVID CORE**
👑 **Owner : @xxbga**
━━━━━━━━━━━━━━━━━━
""",
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
        LOGGER.error(e)

    try:
        os.remove(f"downloads/welcome_{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except:
        pass


# ─────────────────────────────────────────────
# Bot added to new group log
# ─────────────────────────────────────────────
@app.on_message(filters.new_chat_members & filters.group, group=-1)
async def bot_wel(_, message: Message):
    for u in message.new_chat_members:
        if u.id == app.me.id:
            await app.send_message(
                LOG_CHANNEL_ID,
                f"""
➕ **NEW GROUP ADDED**
━━━━━━━━━━━━━━━━━━
📛 **Name** : {message.chat.title}
🆔 **ID** : `{message.chat.id}`
🔗 **Username** : @{message.chat.username}

⚡ **Bot : {app.mention}**
👑 **Owner : @xxbga**
━━━━━━━━━━━━━━━━━━
""",
            )
