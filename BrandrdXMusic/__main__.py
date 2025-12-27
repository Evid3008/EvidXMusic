import asyncio
import importlib
from sys import argv

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from BrandrdXMusic import LOGGER, app, userbot
from BrandrdXMusic.core.call import Hotty
from BrandrdXMusic.misc import sudo
from BrandrdXMusic.plugins import ALL_MODULES
from BrandrdXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "Assistant client variables are missing. Please configure STRING sessions."
        )
        exit()

    await sudo()

    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    for all_module in ALL_MODULES:
        importlib.import_module("BrandrdXMusic.plugins" + all_module)

    LOGGER("EvidXMusic").info("All modules loaded successfully.")

    await userbot.start()
    await Hotty.start()

    # 🔹 CLEAN SHORT STARTUP VIDEO (REPLACED)
    try:
        await Hotty.stream_call(
            "https://files.catbox.moe/ghi3wy.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("EvidXMusic").error(
            "Please enable video chat in your log group before starting the bot."
        )
        exit()
    except Exception:
        pass

    await Hotty.decorators()

    LOGGER("EvidXMusic").info(
        "EVID CORE Music Bot is now running successfully."
    )

    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("EvidXMusic").info("EVID CORE Music Bot stopped cleanly.")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
