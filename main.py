import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio
import random

load_dotenv()
TOKEN = os.getenv('TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'en liñea!')
    try: 
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# loading cogs
async def load_cogs():
    await bot.load_extension('cogs.greek')
    await bot.load_extension('cogs.close')
    await bot.load_extension('cogs.album')
    await bot.load_extension('cogs.quiz')
    # await bot.load_extension('cogs.lyrics')
    await bot.load_extension('cogs.unitcircle')
    await bot.load_extension('cogs.info')
    await bot.load_extension('cogs.say')
async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())