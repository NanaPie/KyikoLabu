import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run('NjI3NzgxODU5NzQ4NzQxMTYx.XZB25A.PNR1oGWLL_7A0DYCtAvvjKOX7GY')
