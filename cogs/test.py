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

    @commands.command(name='countdown', help='counting down from 10 to 0')
    async def countdown(self, ctx):
        number = 10
        msg = await ctx.reply(number)
        await asyncio.sleep(1.0)
        while (number != 0):
            number = number - 1
            await msg.edit(content=number)
            await asyncio.sleep(1.0)

def setup(client):
    client.add_cog(Test(client))