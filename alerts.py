import os

import httpx
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")


def send_alert(message: str):
    if not DISCORD_WEBHOOK_URL:
        print("ERROR: DISCORD_WEBHOOK_URL not set in .env")
        return
    httpx.post(DISCORD_WEBHOOK_URL, json={"content": message}, timeout=10)
