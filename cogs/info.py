import discord
from discord import app_commands
from discord.ext import commands
import asyncio

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="info",description="n/a")
    async def info(self, interaction: discord.Interaction):
        file = discord.File('juegito/juegito bot/images/japanbanner.png',filename='japanbanner.png')
        info_embed = discord.Embed(
            title="❍═══════大日本帝国 Empire of Japan════════❍",
            description="""
                ‣ **Capital:** 東京都 Tokyo
                ‣ **Anthem:** 君が代 Kimigayo 'His Majesty's Reign'

                ❍═════════════════════════════════════❍
                **政府 Government of Japan 🇯🇵**

                ‣ **天皇 Emperor:** <@995777719394635946>
                ‣ **皇后 Empress:** <@883543878479781888>
                ‣ **首相 Prime Minister:** <@431404952402001921>
                *and members of キャビネット Naikaku*

                ❍═════════════════════════════════════❍
                **知事 Governors 🗾**

                ‣ **南日本 Minaminihon:** <@890008517321322506>
                ‣ **中部日本 Chūbunippon:** <@431404952402001921>
                ‣ **北日本 Kitanihon:** <@802208836823154728>
                ‣ **満州国 Manshū kuni** <@865399631235776522>

                ❍═════════════════════════════════════❍
                **組織 Organization 🏯**

                ‣ **天皇 Emperor** <@&1430600705189875733> - *His Majesty, the Emperor of Japan*
                ‣ **首相 Prime Minister** <@&1430607807740117084> - *Head of his Majesty's Government*
                ‣ **元老 Advisor** <@&1430619249109499954> - *Advisors and wise men of His Majesty's Government*
                ‣ **内閣 Cabinet** <@&1432771444688818297> - *Ministers of His Majesty's Government*
                ‣ **陸軍 Army Staff** <@&1432759145680867379> - *Esteemed staff of the Imperial Japanese Army*
                ‣ **知事 Governor** <@&1430610926050087103> - *Provincial Governors of Japan*
                ‣ **市民 Citizen** <@&1430609287180193862> - *Citizen of the Empire of Japan*
                ‣ **外交官 Diplomat** <@&1430778755185512560> - *Foreign representatives to His Majesty's Government*

                ❍══════════════════🇯🇵════════════════❍

                日本 *Land of the Rising Sun*
            """,
            color=discord.Color.from_rgb(44, 47, 51)
        )
        info_embed.set_image(url='attachment://japanbanner.png')
        # channel = self.bot.get_channel(1013841679767318638)
        await interaction.channel.send(file=file,embed=info_embed,)
        
async def setup(bot):
    await bot.add_cog(Info(bot))