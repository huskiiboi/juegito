import discord
from discord import app_commands
from discord.ext import commands
import asyncio

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="say",description="n/a")
    @app_commands.describe(content='content')
    async def info(self, interaction: discord.Interaction, content: str):
        app_info = await self.bot.application_info()
        if interaction.user.id == app_info.owner.id:
            await interaction.channel.send(content)
async def setup(bot):
    await bot.add_cog(Say(bot))