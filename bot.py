import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = 'bc!')

@client.event
async def on_ready():
  print('Bot is ready.')
  
@client.command()
async def hello(ctx):
  print(f'{ctx.author} says hello! (The guild id is {ctx.guild.id} and the guild name is {ctx.guild})!')

client.run(get_env('TOKEN'))
