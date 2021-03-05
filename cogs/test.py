import asyncio
from os import name
from discord.ext import commands
import random

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name='ping', help='Writes back Pong in response')
    async def ping(self,ctx):
        await ctx.send("Pong")

    @commands.command(name='hello', help='hello command for the bot')
    async def hello(self, ctx):
        print(ctx.author)
        await ctx.reply('Hello {0.author}'.format(ctx))

    @commands.command(name='hi', help='hello command with delay')
    async def hi(self, ctx):
        print(ctx.author)
        await asyncio.sleep(5)
        await ctx.reply('Hello {0.author}'.format(ctx))
def setup(client):
    client.add_cog(Test(client))