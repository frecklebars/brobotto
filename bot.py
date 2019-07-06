import discord
import numpy as np

ftoken = open("token/_token.txt", 'r')
TOKEN = ftoken.read()
print(TOKEN)
client = discord.Client()

prefix = 'bro '

@client.event
async def on_message(message):
    #ignore himself
    if message.author == client.user:
        return
    
    if message.content:
        check = np.random.randint(0,100)
        if check < 5:
            await message.channel.send("why are you like this")
    
    if message.content.startswith(prefix):
        msg = message.content
        msg = msg.replace(prefix, "")
        if msg == "hello":
            await message.channel.send("hello!")


@client.event
async def on_ready():
    print("logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("-------------")
    
client.run(TOKEN)