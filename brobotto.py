import discord
import numpy as np

ftoken = open("token/_token.txt", 'r')
TOKEN = ftoken.read()

client = discord.Client()

prefix = 'b!'

@client.event
async def on_message(message):
    #ignore himself
    if message.author == client.user:
        return
    
    #PREFIXED COMMANDS
    if message.content.startswith(prefix):
        msg = message.content
        msg = msg.replace(prefix, "")
        
        if msg == "hello":
            await message.channel.send("hello!")
            return
        
        if msg == "see you later alligator":
            await message.channel.send("in a while crocodile")
            return
            
        elif msg == "color":
            rgb = [np.random.randint(0, 256) for i in range(3)]
            linkrgb = ""
            rgbvalstr = "rgb("
            hexvalstr = "hex: #"
            for i in range(len(rgb)):
                rgbvalstr = rgbvalstr + str(rgb[i]) + ", "
                
                rgb[i] = str(hex(rgb[i]))
                rgb[i] = rgb[i][2:]
                if len(rgb[i]) < 2:
                    rgb[i] = "0" + rgb[i]
                linkrgb += rgb[i]
                
            rgbvalstr = rgbvalstr[:-2] + ")"
            hexvalstr += linkrgb
            await message.channel.send("here's a random color:\n" + rgbvalstr + "\n" + hexvalstr)
            await message.channel.send("https://www.color-hex.com/color/" + linkrgb)
            return
        
    if message.content:
        check = np.random.randint(0,100)
        if check < 5:
            await message.channel.send("why are you like this") #i dont know man i swear im trying,


@client.event
async def on_ready():
    print("logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("-------------")
    
client.run(TOKEN)