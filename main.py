import asyncio
import discord
import os

from discord.ext import commands

from authentication import reddit_authentication
from authentication import discord_authentication

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
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)