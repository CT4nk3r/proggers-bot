import asyncio
import discord

from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

queue = []

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class Music(commands.cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, name='join' , help = 'The bot joins to your voice channel.')
    async def join(self,ctx):
        channel= ctx.message.author.voice.channel
        voice = await channel.connect()  

    @commands.command(name='leave', help='The bot leaves your voice channel.')
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command(name='queue', help = 'This command adds a song to the queue')
    async def add(self,ctx, url):
        global queue

        queue.append(url)
        await ctx.send(f'`{url}` added to queue!')

    @commands.command(name='remove', help='This command removes an item from the list')
    async def remove(self,ctx, number):
        global queue

        try:
            del(queue[int(number)])
            await ctx.send(f'Your queue is now `{queue}!`')
    
        except:
            await ctx.send('Your queue is either **empty** or the index is **out of range**')

    @bot.command(name='view', help='This command shows the queue')
    async def view(self,ctx):
        await ctx.send(f'Your queue is now `{queue}!`')

    @commands.command(name='play', help='This command plays songs')
    async def play(self,ctx):
        global queue

        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            player = await YTDLSource.from_url(queue[0], loop=bot.loop)
            voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('**Now playing:** {}'.format(player.title))
        del(queue[0]) 
    
    @commands.command(name='pause', help='This command pauses the song')
    async def pause(self,ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client

        voice_channel.pause()

    @commands.command(name='resume', help='This command resumes the song!')
    async def resume(self,ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client

        voice_channel.resume()  

    @bot.command(name='stop', help='This command stops the song!')
    async def stop(self,ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client

        voice_channel.stop()

def setup(client):
    client.add_cog(Music(client))