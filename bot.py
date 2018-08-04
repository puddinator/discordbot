import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


client = commands.Bot(command_prefix = "$")


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")


@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)             
        

client.run('NDc1MTgyOTY4NDQ5NTMxOTE2.Dkb-MA.skbs9W1IsXkax-xLOrhGh9ed380')

