import discord
import requests
import json

# update the url to https://meme-api.com/gimme
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('Dame un meme'):
            await message.channel.send(get_meme())
        if message.content.startswith('Hello'):
            await message.channel.send('Bienvenido bro!')

# create intents keyword argument
intents = discord.Intents.default()
intents.message_content = True

# update the call here by passing the 'intents' keyword argument
client = MyClient(intents=intents)
client.run('MTM2MTA3NzU2ODgwMzA0OTc0Ng.G7ItjU.Inka7tvVcsnvfUmFJayvr1zaYvRXlBTm4Y6_cM')

