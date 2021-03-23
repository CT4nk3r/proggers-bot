# proggers-bot

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Ez egy reddit és discord bot lesz, ami átjárást biztosít a két platform között. Megosztva egymással mind a kettő tartalmát.

## Technologies
Project is created with:
* Python version: 3.8.7
* discord.py: 1.6.0
* pip: 21.0.1
* praw: 3.6.0
* Visual Studio Code
* Discord
* Reddit

## Setup
To run this project, install a running enviroment for python, download praw and 

authentication should happen in a different file:
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

Botunk képes letölteni képeket egy adott subredditről, hot, new, top orderben, ehez csak be kell írni, hogy: "!download sub limit order" #ahol a sub egy subreddit neve legyen, a limit a kívánt mennyiség az order pedig a rangsorolás menete

