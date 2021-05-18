import asyncio
import discord
import os

from discord.ext import commands

from authentication import reddit_authentication
from authentication import discord_authentication
from yahoofinancials import YahooFinancials
import time

print("Authenticating discord bot...")
TOKEN = discord_authentication()
print("Authenticating reddit bot...")
reddit = reddit_authentication()
print("Reddit authentication as: {}".format(reddit.user.me()))
subreddit = reddit.subreddit('memes')
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    # channel = bot.get_channel(816668887407132715)
    # await channel.send('Status changed to online')
    print('Discord authentication as: {0.user}'.format(bot))
    activity = discord.Game(name='https://github.com/CT4nk3r/proggers-bot')
    await bot.change_presence(activity=activity)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.event
async def logout():
    await bot.logout()

@bot.command()
@commands.has_role("Developers")
async def load(ctx, extension):
    try:
        bot.load_extension(f'cogs.{extension}')
    except commands.MissingRole:
       await ctx.send('You do not have the correct role for this command.')

@bot.command()
@commands.has_role("Developers")
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
    except commands.MissingRole:
       await ctx.send('You do not have the correct role for this command.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

"""
async def timetravel():
    await bot.wait_until_ready()
    await asyncio.sleep(1.5)
    channel = bot.get_channel(844237645344669736)
    ticker = 'GME'
    ticker2 = 'AAPL'
    ticker3 = 'AMC'
    ticker4 = 'AMD'
    ticker5 = 'INTC'
    while not bot.is_closed():
        my_stock = YahooFinancials(ticker)
        price = my_stock.get_current_price()
        await channel.send( f"{ticker}  right now is on : ")
        await channel.send (price)
        my_stock2 = YahooFinancials(ticker2)
        price2 = my_stock2.get_current_price()
        await channel.send(f"{ticker2} right now is on : ")
        await channel.send (price2)
        my_stock3 = YahooFinancials(ticker3)
        price3 = my_stock3.get_current_price()
        await channel.send( f"{ticker3} right now is on : ")
        await channel.send (price3)
        my_stock4 = YahooFinancials(ticker4)
        price4 = my_stock4.get_current_price()
        await channel.send(f"{ticker4} right now is on : ")
        await channel.send (price4)
        my_stock5 = YahooFinancials(ticker5)
        price5 = my_stock5.get_current_price()
        await channel.send(f"{ticker5} right now is on : ")
        await channel.send (price5)
        await asyncio.sleep(3)

bot.loop.create_task(timetravel())"""

bot.run(TOKEN)