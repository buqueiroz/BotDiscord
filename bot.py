import discord
from discord.ext import commands

bot = commands.Bot("!")


@bot.event
async def on_ready():
  print("Estou pronto! Estou como {bot.user}")


@bot.command(name="oi")
async def send_hello(ctx):
  name = ctx.author.name

  response = "ola, " + name

  await ctx.send(response)


bot.run('token bot')