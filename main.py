import discord
import os


class MyClient(discord.Client):

  async def on_ready(self):
    print(f'{self.user} is logged in')

  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('%hello'):
      await message.channel.send('sugi pula')
      
    if message.content.startswith('👍'):
      await message.channel.send('😂👌')
      
    if message.author != self.user:
      print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['TOKEN'])
