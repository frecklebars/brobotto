import discord
import random
import numpy as np
import time

import brolines


ftoken = open("token/_token.txt", 'r')
TOKEN = ftoken.read()

client = discord.Client()

prefix = 'b!'
excluded = ["etika", "bruh", "sex"]

excluded_channels = [388977036443779072]

BRO_HAUS_ID = 387676518077300736
BTTRDTST_ID = 727537357502283778
FRECKLEBARS_ID = 194384963615850496

@client.event
async def on_message(message):
    
    #no instant reply
    time.sleep(0.15)
        
    #ignore himself
    if message.author == client.user:
        return
    
    if message.channel.id in excluded_channels:
        return
    
    #PREFIXED COMMANDS
    if message.content.startswith(prefix):
        msg = message.content.lower()
        msg = msg.replace(prefix, "")
        
        if np.random.randint(0, 100) < 10:
            if msg not in excluded:
                await message.channel.send("no")
                return
        
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
        
        if msg in ["isepic", "is epic"]:
            await message.channel.send("what is epic?")
            return
        if msg.startswith("isepic") or msg.startswith("is epic"):
            msg = msg.replace("isepic ", "")
            chance = np.random.randint(0,2)
            if chance == 1:
                await message.channel.send("ok " + msg + " is epic")
                return
            else:
                await message.channel.send("ok " + msg + " is not epic")
                return
            
        if msg == "bruh" or msg == "bruh moment":
            await message.channel.send(file = discord.File("bruh.jpg"))
            await message.channel.send("bruh")
            
        """
        if msg == "pokemon":
            await message.channel.send("https://pokemondb.net/pokedex/" + str(np.random.randint(1, 894)))
            return
        if msg.startswith("pokemon "):
            msg = msg.replace("pokemon ", "")
            if msg == "gen" or msg == "gen ":
                await message.channel.send("you need to specify a generation from 1 to 8\nfor example `b!pokemon gen 4`")
                return
            if msg.startswith("gen "):
                msg = msg.replace("gen ", "")
                gen = int(msg)-1
                if gen not in range(0, 8):
                    await message.channel.send("no such generation exists")
                    return
                genindex = [[1, 152], [152, 252], [252, 387], [387, 494], [494, 650], [650, 722], [722, 810], [810, 894]]
                await message.channel.send("https://pokemondb.net/pokedex/" + str(np.random.randint(genindex[gen][0], genindex[gen][1])))
                return
        """
        
        if msg == "help":
            await message.channel.send("you can see the shid i do here:\nhttps://github.com/frecklebars/brobotto/blob/master/README.md")
            return
        
        if msg == "sex":
            await message.channel.send("https://www.youtube.com/watch?v=MUhxQ8dEr-w")
            return
        
        if msg == "etika":
            pic = np.random.randint(1, 44)
            etikafile = "etika/" + str(pic) + ".jpg"
            await message.channel.send(file = discord.File(etikafile, filename = "etika.jpg"))
            return
        
        if msg == "await message.channel.send":
            line = np.random.randint(0, len(brolines.quotes))
            await message.channel.send(brolines.quotes[line])
            return
        
        if msg == "judgement":
            joshu = np.random.randint(0, 2)
            if joshu == 1:
                await message.channel.send(file = discord.File("img/joshu/epic.jpg"))
            else:
                await message.channel.send(file = discord.File("img/joshu/cringe.png"))
        
        if msg == "weather":
            await message.channel.send("please specify a city")
            return
        if msg.startswith("weather "):
            import weatherbro as wb
            msg = msg.replace("weather ", "")
            weatherreport = wb.getw(msg)
            await message.channel.send(weatherreport)
            return
                
        #DEBUG
        if message.author.id == FRECKLEBARS_ID:
            if msg == "kill":
                await message.channel.send(":(")
                exit()
            if msg.startswith("debug "):
                msg = msg.replace("debug ", "")
                if msg == "ping":
                    await message.channel.send("poong")
                    
                if msg == "serverlist":
                    print("===current servers im in===")
                    for server in client.guilds:
                        print(server.name)
                    print("===========================")
                    return
                
                if msg == "spitid":
                    await message.channel.send(message.channel.id)
                    return
                
            
    #NON PREFIXED
    msg = message.content.lower()
    if msg == "see you later alligator":
        await message.channel.send("in a while crocodile")
        return
    
    if msg.find("69") >= 0:
        if "69" in msg.split():
            await message.channel.send("nice")
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
        return
            
    if msg.find("bro") >= 0:
        if msg.find("brobotto") >= 0:
            return
        ochance = np.random.randint(0, 5)
        dotchance = np.random.randint(0, 15)
        await message.channel.send("bro" + "o" * ochance + "." * dotchance)
        return
    
    if msg.find("based") >= 0 and msg.find("based on what") == -1:
        await message.channel.send("based on what")
        return
    
    for lfg in brolines.lfgVariants:
        if msg.find(lfg) >= 0:
            if np.random.randint(0, 100) < 30:
                await message.channel.send("go where")
                return
            lfgOCnt = np.random.randint(7, 30)
            await message.channel.send("LETS FUCKING GO" + "O" * lfgOCnt)
            return

    #BRO HAUS SPECIFIC
    if message.guild.id == BRO_HAUS_ID:
        if np.random.randint(0, 100) < 3:
            emoji = discord.utils.get(message.guild.emojis, name=random.choice(brolines.reactEmojisBroHaus))
            if emoji:
                await message.add_reaction(emoji)
    
    #LAST
    if msg:
        check = np.random.randint(0,1000)
        if check < 7:
            line = np.random.randint(0, len(brolines.quotes))
            await message.channel.send(brolines.quotes[line])
        return

@client.event
async def on_ready():
    print("logged in as: " + str(client.user.name))
    print("id: " + str(client.user.id))
    print("----------------------")
    print("yep, it's bro time\n")
	
    
client.run(TOKEN)
