import discord
import os
#discord (up) client loader(down)
client = discord.Client()

#messages
@client.event
async def on_ready():
    print("Hello, I'm {0.user}. Hello World ")


@client.event
async def onmessage(message):
    if message.author == client.user:
        return

#Token environment variable link
my_secret = os.environ['token']