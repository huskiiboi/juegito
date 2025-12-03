import discord
from discord import app_commands
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

class Album(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        authorization = SpotifyClientCredentials(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
        )
        self.sp = spotipy.Spotify(client_credentials_manager=authorization) # authorizing use of spotify api
    
    @app_commands.command(name="album",description="retrieve an album from spotify's api")
    @app_commands.describe(album_name="album name")
    async def album(self,interaction: discord.Interaction, album_name: str):
        await interaction.response.defer()
        try:
            result = self.sp.search(q=album_name, type='album', limit=1)

            if not result['albums']['items']:
                await interaction.followup.send('☹️ no album found')
                return

            album = result['albums']['items'][0]

            track_info = self.sp.album_tracks(album['id'])
            tracks = ""

            for i, track in enumerate(track_info['items']):
                tracks += f"➢ *{track['name']}*\n"

            embed = discord.Embed(
                title=album['name'],
                description=f"by **{album['artists'][0]['name']}**\n\n {tracks}\n",
                color = discord.Color.from_rgb(44, 47, 51)
            )

            embed.set_image(url=album['images'][0]['url'])

            await interaction.followup.send(embed=embed)
        except Exception as e:
            await interaction.followup.send(f'Error: {str(e)}')

async def setup(bot):
    await bot.add_cog(Album(bot))