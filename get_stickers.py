import asyncio
import os

from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon import functions, types

load_dotenv(".env", override=True)

# Load environment variables
SESSION_NAME = os.environ["SESSION_NAME"]
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]


async def get_user_sets():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    async with client:
        stickerSets = await client(functions.messages.GetAllStickersRequest(
            hash=-1237456826
        ))
        return stickerSets.sets