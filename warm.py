import random
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    for guild in bot.guilds:
        for channel in guild.text_channels:
            with open ('Texts/start.txt','r', encoding='UTF-8')as f:
                await channel.send(f.read())
      
@bot.command()
async def global_warm(ctx):
    with open ('Texts/gw.txt','r', encoding='UTF-8')as f:
        await ctx.send(f.read())

@bot.command()
async def reasons(ctx):
    with open ('Texts/prich.txt','r', encoding='UTF-8')as f:
        await ctx.send(f.read())

@bot.command()
async def consequences(ctx):
    with open ('Texts/posl.txt','r', encoding='UTF-8')as f:
        await ctx.send(f.read())

@bot.command()
async def human(ctx):
    with open ('Texts/man.txt','r', encoding='UTF-8')as f:
        await ctx.send(f.read())


bot.run("")