# Proggers-bot   
<p align="center">
  <img src="logo.png" />
</p>
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Ez egy reddit és discord bot lesz, ami átjárást biztosít a két platform között. Megosztva egymással mind a kettő tartalmát. Botunk képes letölteni képeket egy adott subredditről, hot, new, top orderben, ehez csak be kell írni, hogy: `!download sub limit order` ahol a sub egy subreddit neve legyen, a limit a kívánt mennyiség az order pedig a rangsorolás menete.

## Technologies
Project is created with:
* Python version: 3.8.7 :snake:
* discord.py: 1.6.0
* pip: 21.0.1
* praw: 3.6.0

## Setup
To run this project, install a running enviroment for python, download praw and discord.py 
First of all, we have to install Python from [here](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe).
Now we have to use python to download the modules that we need, mainly we are using discordpy and praw. 
Open up the python terminal and type in to download discordpy: `pip install -U discord.py`
Then we are going to download praw with this: `pip install praw`


Then make an authentication file that should look something like this:
```
#authentication.py

import praw
def reddit_authentication():
    print("Authenticating...")
    reddit = praw.Reddit(client_id="[CLIENT_ID]]",
                     client_secret="[SECRET]]",
                     username="[USERNAME]",
                     password="[PASSWORD]",
                     user_agent="[DESCRIPTION OF BOT]]")
    return reddit

def discord_authentication():
    return 'DISCORD_TOKEN'
#token should be at https://discord.com/developers/applications/00000000000000/bot -> token -> copy
```
