import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("Hello, I'm {0.user}. Hello World ")


@client.event
async def onmessage(message):
    if message.author == client.user:
        return


my_secret = os.environ['token']
