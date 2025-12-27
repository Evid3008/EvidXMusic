"""
────────────────────────────────────────────────────────────────────────
███████╗██╗   ██╗██╗██████╗     ██████╗ ██████╗ ██████╗ ███████╗
██╔════╝██║   ██║██║██╔══██╗   ██╔════╝██╔═══██╗██╔══██╗██╔════╝
█████╗  ██║   ██║██║██║  ██║   ██║     ██║   ██║██████╔╝█████╗  
██╔══╝  ╚██╗ ██╔╝██║██║  ██║   ██║     ██║   ██║██╔══██╗██╔══╝  
███████╗ ╚████╔╝ ██║██████╔╝   ╚██████╗╚██████╔╝██║  ██║███████╗
╚══════╝  ╚═══╝  ╚═╝╚═════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

                    E V I D   C O R E
────────────────────────────────────────────────────────────────────────
"""

from typing import Dict, Union
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from config import MONGO_DB_URI

mongo = MongoCli(MONGO_DB_URI)

# 🔁 IDENTITY CHANGED HERE
db = mongo.EvidXMusic

coupledb = db.couple
afkdb = db.afk
nightmodedb = db.nightmode
notesdb = db.notes
filtersdb = db.filters

async def _get_lovers(cid: int):
    lovers = await coupledb.find_one({"chat_id": cid})
    if lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers

async def _get_image(cid: int):
    lovers = await coupledb.find_one({"chat_id": cid})
    if lovers:
        lovers = lovers["img"]
    else:
        lovers = {}
    return lovers

async def get_couple(cid: int, date: str):
    lovers = await _get_lovers(cid)
    if date in lovers:
        return lovers[date]
    else:
        return False

async def save_couple(cid: int, date: str, couple: dict, img: str):
    lovers = await _get_lovers(cid)
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": cid},
        {"$set": {"couple": lovers, "img": img}},
        upsert=True,
    )
