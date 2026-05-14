import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.
default()
intents.menssage_content = True

bot = commands.bot
(command_prefix = '$' , intents = intents)

@bot.event
async def on_ready():
    print (f'fizemo login como {bot.user}')

@bot.event
async def on_messsage(message):
    if message.autor == bot.user :
        return
    
    await bot.process_commands(message)

async def hello(ctx) :
    await ctx.send('hi')

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

bot.command()
async def senha(ctx):
    await ctx.send('sua senha :' + gen_pass(10))

bot.command()
async def test(ctx , arg):
    await ctx.send(arg)

bot.run('TOKEN')
    


