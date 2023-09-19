import discord
from config import API_DISCORD
from chatgpt import gpt


class DiscordClient(discord.Client):

    async def on_ready(self):
        print ("Iniciando ... ")

    async def on_message(self,message):

        if self.user== message.author:
         return
        elif message.content.startswith("/bot"):
            question= message.content.replace("/bot", "")
            answer= gpt(question) 
            await message.channel.send(answer)
    
intents = discord.Intents.default() 
intents.message_content = True
client = DiscordClient(intents=intents)
client.run(API_DISCORD)