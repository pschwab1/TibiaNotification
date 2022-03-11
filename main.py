import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user})'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$test'):
    await message.channel.send('Tiago é uma bicha!')

  if message.content.startswith('$respleave'):
    text = message.content
    text = text.replace('$respleave','')
    await message.channel.send('Respawn'+text+' livre')

client.run(os.getenv('TOKEN'))