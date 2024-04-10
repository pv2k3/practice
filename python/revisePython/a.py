import trio
import httpx

from holehe.modules.social_media.discord import discord

async def main():
    email = "ov3644111@gmail.com"
    out = []
    client = httpx.AsyncClient()

    await discord(email, client, out)

    print(out)
    await client.aclose()

trio.run(main)
