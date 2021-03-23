from os import name
from typing import NewType
from discord.ext import commands
from praw.const import MAX_IMAGE_SIZE
from main import subreddit

class Reddit(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name='meme', help='shows you the latest meme on r/memes')
    async def meme(self, ctx):
        new_meme = subreddit.new(limit=1)
        for meme in new_meme:
            print(meme)
            print(meme.url)
            await ctx.send(meme.url)

    # @commands.command(name='download', help='downloads the best pictures from the chosen subreddit')
    # async def download(self, ctx, sub : str, limit : int, order : str):
        

def setup(client):
    client.add_cog(Reddit(client))