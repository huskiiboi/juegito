import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import random

class Greek(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="greek", description="greek alphabet quiz")
    async def greek(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{interaction.user.mention} beginning greek quiz...')

        greek_alphabet_names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta','iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho','sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']
        greek_alphabet = ['Αα', 'Ββ', 'Γγ', 'Δδ', 'Εε', 'Ζζ', 'Ηη', 'Θθ', 'Ιι', 'Κκ', 'Λλ', 'Μμ', 'Νν', 'Ξξ', 'Οο', 'Ππ', 'Ρρ', 'Σσ', 'Ττ', 'Υυ', 'Φφ', 'Χχ', 'Ψψ', 'Ωω']

        for letter in range(len(greek_alphabet)):

            number = letter + 1

            await interaction.channel.send(f'{number}: what is this letter? {greek_alphabet[letter]}')

            def check(message):
                return message.author == interaction.user and message.channel == interaction.channel
            try:
                response = await self.bot.wait_for('message', check=check, timeout=30.0)
                if response.content.lower() == greek_alphabet_names[letter]:
                    await interaction.channel.send(f'✅ correcto. symbol: {greek_alphabet[letter]}, name: {greek_alphabet_names[letter]}')
                elif response.content.lower() == 'exit':
                        await interaction.channel.send('exiting quiz...')
                        break
                else:
                    await interaction.channel.send(f'❌ incorrecto. {greek_alphabet[letter]} was {greek_alphabet_names[letter]}')
            except asyncio.TimeoutError:
                await interaction.channel.send('timeout')
                break
        await interaction.channel.send('quiz ended...')
    
async def setup(bot):
    await bot.add_cog(Greek(bot))