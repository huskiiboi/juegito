import discord
from discord.ext import commands
import asyncio

class UnitCircle(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def unitcircle(self, ctx):

        complete_circle = "juegito/juegito bot/images/complete unit circle.png"
        incomplete_circle = "juegito/juegito bot/images/incomplete unit circle.png"
        # making into discord files
        file_1 = discord.File(complete_circle, filename='complete_circle.png')
        file_2 = discord.File(incomplete_circle, filename='incomplete_circle.png')
        # from 1-3
                # [coordinate, radian, degrees]
        key = {
            'a': ['(1,0)', '0', '0'],
            'b': ['(√3/2, 1/2)', 'π/6', "30"],
            'c': ['(√2/2, √2/2)', 'π/4', "45"],
            'd': ['(1/2, √3/2)', 'π/3', "60"],
            'e': ['(0,1)', 'π/2', '90'],
            'f': ['(-1/2, √3/2)', '2π/3', '120'],
            'g': ['(-√2/2, √2/2)', '3π/4', '135'],
            'h': ['(-√3/2, 1/2)', '5π/6', '150'],
            'i': ['(-1,0)', 'π', '180'],
            'j': ['(-√3/2, -1/2)', '7π/6', '210'],
            'k': ['(-√2/2, -√2/2)', '5π/4', '225'],
            'l': ['(-1/2, -√3/2)', '4π/3', '240'],
            'm': ['(0,-1)', '3π/2', '270'],
            'n': ['(1/2,-√3/2)', '5π/3', '300'],
            'o': ['(√2/2, -√2/2)', '7π/4', '315' ],
            'p': ['(√3/2, -1/2)', '11π/6', '330']
        }

        await ctx.send(f'🎓 beginning the unit circle series quiz\n send "help" at any point to see the complete unit circle')
        for index, series in key.items():
            file_2 = discord.File(incomplete_circle, filename='incomplete_circle.png')

            embed = discord.Embed(
                title=f'unit circle: series {index}',
                description= f'find the three values (sub 1, 2, and 3) for {index}',
                color= discord.Color.from_rgb(44, 47, 51),
            )
            resources = discord.Embed(
                title='special chars',
                description=f'√ π',
                color = discord.Color.from_rgb(44,47,51)
            )
            embed.set_image(url='attachment://incomplete_circle.png')
            await ctx.send(file=file_2,embed=embed)
            await ctx.send(embed=resources)

            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel
                        
            await ctx.send(f'what is the **coordinate** point for {index}_1')
            response = await self.bot.wait_for('message', check=check, timeout=60.0)
            # coordinate
            if response.content == series[0]:
                await ctx.send(f'✅ correct, the coordinate was {series[0]}')
            else:
                await ctx.send(f'❌ incorrect, the coordinate was {series[0]}')
            
            await ctx.send(f'what is the **radian angle** point for {index}_2')
            response = await self.bot.wait_for('message', check=check, timeout=60.0)
            # radian angle
            if response.content == series[1]:
                await ctx.send(f'✅ correct, the radian angle was {series[1]}')
            else:
                await ctx.send(f'❌ incorrect, the radian angle was {series[1]}')
        
            await ctx.send(f'what is the **degree** point for {index}_3')
            response = await self.bot.wait_for('message', check=check, timeout=60.0)
            # degree
            if response.content == series[2]:
                await ctx.send(f'✅ correct, the degree was {series[2]}')
            else:
                await ctx.send(f'❌ incorrect, the degree was {series[2]}')
async def setup(bot):
    await bot.add_cog(UnitCircle(bot))