from dotenv import load_dotenv
import discord
import os

load_dotenv()

#set up intents
intents = discord.Intents.default()
intents.message_content = True #ensure that your bot can read message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client.user))

@client.event
async dev on_message(messsage):
  if message.author == client.user:
    return
    
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
