import discord
from discord.ext import commands
import asyncio

class Quiz(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def quiz(self,ctx):
        questions = {
            "what chapter are we?": "delta chapter",
            "founded on?": "november 9 2017",
            "maxim": "for the love of technology",
            "president": "danny whelan",
            "vice president": "jaspreet singh",
            "director of engagement": "alexandra miller-thomas",
            "director of professional development": "kymani hughes",
            "treasurer": "madison lee",
            "director of public relations": "ayush sawant",
            "director of technology": "hiram hackworth",
            "director of membership": "charles fleckenstein",
            "color 1": "blue #458FFF",
            "color 2": "green #19FF19",
            "kappa": "community",
            "theta": "of wisdom and teacher",
            "pi": "passion",
            "national mascot": "ninja",
            "syracuse mascot": "klippy",
            "founder 1": "mackenzie corcoran",
            "founder 2": "sophie estep",
            "founder 3": "ryan french",
            "founder 4": "max keiser",
            "founder 5": "kieran o'halloran",
            "founder 6": "mason rosenthal",
            "founder 7": "dominic serrao",
            "founder 8": "seth weingarten",
            "chatper is when?": "sunday 1pm",
            "most recent chapter": "alpha gamma @ virginia tech"
        }

        for question, answer in questions.items():
            await ctx.send(f'topic: {question}')
            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel
            try:
                response = await self.bot.wait_for('message', check=check, timeout=30.0)
                if response.content.lower() == answer:
                    await ctx.send(f'✅ correcto, answer was {answer}')
                elif response.content.lower() == 'exit':
                    await ctx.send('exiting quiz...')
                    break
                else:
                    await ctx.send(f'❌ incorrecto, answer was {answer}')
            except asyncio.TimeoutError:
                await ctx.send('timeout')
                break
        await ctx.send('quiz ended...')
async def setup(bot):
    await bot.add_cog(Quiz(bot))