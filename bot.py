import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1064859670101114942)
    await channel.send(F'{member} 混進來了!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1064859670101114942)
    await channel.send(F'{member} 滾了!')

bot.run('MTA4MDc0NzczMzU5MTI2MTE5NQ.GRL0IO.Y_HVr6kvt1UUtzTkuyOZIjBaSmEyOeg6_mboRk')