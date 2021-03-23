import asyncio
from os import name
from discord.ext import commands
import random
import os
import re
from praw.const import MAX_IMAGE_SIZE
import requests
import praw
import configparser
import concurrent.futures
import argparse
from praw import reddit
from main import subreddit

class Reddit(commands.Cog):

    def __init__(self, client):
        self.client = client
        config = configparser.ConfigParser()
        config.read('conf.ini')
        self.path = f'downloaded/'
    
    @commands.command(name='meme', help='shows you the latest meme on r/memes')
    async def meme(self, ctx):
        new_meme = subreddit.new(limit=1)
        for meme in new_meme:
            print(meme)
            print(meme.url)
            await ctx.send(meme.url)

    @commands.command(name='download', help='downloads the best pictures from the chosen subreddit')
    async def download(self, ctx, sub : str, limit : int, order : str):
        images = []
        try:
            go = 0
            if order == 'hot':
                submissions = reddit.subreddit(sub).hot(limit=None)
            elif order == 'top':
                submissions = reddit.subreddit(sub).top(limit=None)
            elif order == 'new':
                submissions = reddit.subreddit(sub).new(limit=None)
            for submission in submissions:
                if not submission.stickied and submission.url.endswith(('jpg', 'jpeg', 'png')):
                    fname = self.path + re.search('(?s:.*)\w/(.*)', submission.url).group(1)
                    if not os.path.isfile(fname):
                        images.append({'url': submission.url, 'fname': fname})
                        go += 1
                        if go >= limit:
                            break
            if len(images):
                if not os.path.exists(self.path):
                    os.makedirs(self.path)
                with concurrent.futures.ThreadPoolExecutor() as ptolemy:
                    ptolemy.map(self.download, images)
        except Exception as e:
            print(e)

def setup(client):
    client.add_cog(Reddit(client))