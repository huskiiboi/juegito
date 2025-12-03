import discord
from discord.ext import commands
import asyncio

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def close(self, ctx):
        await ctx.send("closing...")
        await self.bot.close()

async def setup(bot):
    await bot.add_cog(Admin(bot))