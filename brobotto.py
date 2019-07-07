import discord
import numpy as np
import brolines


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
        msg = message.content.lower()
        msg = msg.replace(prefix, "")
        
        if msg == "hello":
            await message.channel.send("hello!")
            return
            
        if msg == "color":
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
        
        if msg == "isepic":
            await message.channel.send("what is epic?")
            return
        if msg.startswith("isepic"):
            chance = np.random.randint(0,2)
            if chance == 1:
                await message.channel.send("ok this is epic")
                return
            else:
                await message.channel.send("ok this is not epic")
                return
        
            
    #NON PREFIXED
    msg = message.content.lower()
    if msg == "see you later alligator":
            await message.channel.send("in a while crocodile")
            return
        
    if (msg.find("pee") >=0) or (msg.find("poo") >=0):
        msg = msg.split(" ")
        if "pee" in msg:
            await message.channel.send("poo")
            return
        if "poo" in msg:
            await message.channel.send("pee")
        return
    
    if msg.find(":)") >= 0:
        await message.channel.send(":)")
            
    if msg.find("bro") >= 0:
        ochance = np.random.randint(0, 5)
        dotchance = np.random.randint(0, 15)
        await message.channel.send("bro" + "o" * ochance + "." * dotchance)
        return


    #LAST
    if msg:
        check = np.random.randint(0,100)
        if check < 5:
            line = np.random.randint(0, len(brolines.quotes))
            await message.channel.send(brolines.quotes[line])
        return

@client.event
async def on_ready():
    print("logged in as: " + str(client.user.name))
    print("id: " + str(client.user.id))
    print("----------------------")
    print("yep, it's bro time")
    
client.run(TOKEN)