import discord
import os 
import requests
import json


players = {}

client = discord.Client()


      

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))



  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith(''):
      if message.author.id == :
        await message.channel.send('')
    else:
      await message.channel.send('nope')


  

client.run(os.getenv('TOKEN'))
