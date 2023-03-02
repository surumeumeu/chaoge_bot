import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utF8') as jFile:
    jdata = json.load(jFile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents = intents)

#調用 event 函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', bot.user)

@bot.event
#當有訊息時
async def on_message(message):
    keyword = ['大便', '便', '我要大便', '小便', '廁所', '拉屎', '我要拉屎']


    #排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content in keyword:
        pic = discord.File('C:\\Users\\Nestia\\Documents\\GitHub\\chaoge_bot\\pic\\ECBFABC7-9390-4773-8E87-0603C1B23CA9.jpg')
        await message.channel.send(file= pic)
        


@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def 我要大便(ctx):
    pic = discord.File('C:\\Users\\Nestia\\Documents\\GitHub\\chaoge_bot\\pic\\ECBFABC7-9390-4773-8E87-0603C1B23CA9.jpg')
    await ctx.send(file= pic)

@bot.command()
async def 大便(ctx):
    pic = discord.File('C:\\Users\\Nestia\\Documents\\GitHub\\chaoge_bot\\pic\\ECBFABC7-9390-4773-8E87-0603C1B23CA9.jpg')
    await ctx.send(file= pic)




@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(F'{member} 混進來了!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(F'{member} 滾了!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} (ms)')

bot.run(jdata['TOKEN'])