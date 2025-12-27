import os
import shutil
from re import findall

from bing_image_downloader import downloader
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message

from BrandrdXMusic import app
from BrandrdXMusic.utils.database import get_sudoers
from config import OWNER_ID


@app.on_message(filters.command(["imgs", "image"], prefixes=["/", "!"]))
async def google_img_search(client: Client, message: Message):
    user_id = message.from_user.id

    # 🔒 OWNER + SUDO ONLY
    sudo_users = await get_sudoers()
    if user_id != OWNER_ID and user_id not in sudo_users:
        return await message.reply(
            "🚫 **Access Denied**\n\n"
            "🧠 **EVID AI Vision** is restricted to **Core Admins only**."
        )

    chat_id = message.chat.id

    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply(
            "🧠 **EVID AI Vision**\n\n"
            "Provide a search query to generate images."
        )

    # limit handling
    lim = findall(r"lim=\d+", query)
    try:
        lim = int(lim[0].replace("lim=", ""))
        query = query.replace(f"lim={lim}", "")
    except IndexError:
        lim = 5  # default limit

    download_dir = "downloads"

    try:
        downloader.download(
            query,
            limit=lim,
            output_dir=download_dir,
            adult_filter_off=True,
            force_replace=False,
            timeout=60,
        )

        images_dir = os.path.join(download_dir, query)
        if not os.listdir(images_dir):
            raise Exception("No images generated.")

        images = [
            os.path.join(images_dir, img)
            for img in os.listdir(images_dir)
        ][:lim]

    except Exception as e:
        return await message.reply(
            f"❌ **EVID AI Error**\n\n`{e}`"
        )

    msg = await message.reply(
        "🧠 **EVID AI Vision**\n\n"
        "🔍 Analyzing & generating images…"
    )

    count = 0
    for _ in images:
        count += 1
        await msg.edit(
            f"🧠 **EVID AI Vision**\n\n"
            f"⚡ Processing `{count}/{lim}`"
        )

    try:
        await app.send_media_group(
            chat_id=chat_id,
            media=[InputMediaPhoto(media=img) for img in images],
            reply_to_message_id=message.id,
        )

        shutil.rmtree(images_dir)
        await msg.delete()

    except Exception as e:
        await msg.delete()
        return await message.reply(
            f"❌ **Failed to send images**\n\n`{e}`"
        )
