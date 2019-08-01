import requests

key = open("token/_weather.txt", 'r')
OWMKEY = key.read()

def kelvintoC(degree):
    return degree - 273.15
def kelvintoF(degree):
    return kelvintoC(degree) *9/5 + 32

emotes = {"01": ":sunny:",
          "02": ":white_sun_small_cloud:",
          "03": ":white_sun_cloud:",
          "04": ":cloud:",
          "09": ":cloud_rain:",
          "10": ":white_sun_rain_cloud:",
          "11": ":cloud_lightning:",
          "13": ":snowflake:",
          "50": ":dash:"
          }

def getw(city):
    url = "http://api.openweathermap.org/data/2.5/weather?appid=" + OWMKEY
    url = url + "&q=" + city
    
    rawdata = requests.get(url).json()
    
    data = {"C": {},
            "F": {}}
    
    #troubleshooting
    msg = ""
    data["code"] = int(rawdata["cod"])
    if data["code"] == 404:
        msg = "city not found"
    elif data["code"] == 429:
        msg = "maximum data inquiries exceeded"
    elif data["code"] == 401:
        msg = "error regarding API key, reach out to https://twitter.com/frecklebars for assistance"
    elif data["code"] == 500:
        msg = "internal server error"
    elif data["code"] == 200:
        
        #TEMPERATURE
        data["C"]["temp"] = "{:+.2f}".format(kelvintoC(rawdata["main"]["temp"])) + "°C"
        data["F"]["temp"] = "{:+.2f}".format(kelvintoF(rawdata["main"]["temp"])) + "°F"
        
        data["C"]["max"] = "{:+.2f}".format(kelvintoC(rawdata["main"]["temp_max"])) + "°C"
        data["F"]["max"] = "{:+.2f}".format(kelvintoF(rawdata["main"]["temp_max"])) + "°F"
        
        data["C"]["min"] = "{:+.2f}".format(kelvintoC(rawdata["main"]["temp_min"])) + "°C"
        data["F"]["min"] = "{:+.2f}".format(kelvintoF(rawdata["main"]["temp_min"])) + "°F"
        
        #WEATHER DESCRIPTION
        data["wdesc"] = rawdata["weather"][0]["description"]
        data["emote"] = emotes[rawdata["weather"][0]["icon"][:-1]]
        
        #MORE WEATHER DATA
        data["humidity"] = str(rawdata["main"]["humidity"]) + "%"
        data["wind"] = str(rawdata["wind"]["speed"]) + " m/s"
        data["clouds"] = str(rawdata["clouds"]["all"]) + "%"
        
        #EXTRA
        data["location"] = rawdata["name"] + ", " + rawdata["sys"]["country"]
        data["flag"] = ":flag_" + rawdata["sys"]["country"].lower() + ":"
        
        ###MESSAGE###
        msg = "Weather report for **" + data["location"] + "** " + data["flag"] + "\n"
        msg += "**Temperature:** " + data["C"]["temp"] + " / " + data["F"]["temp"] + " >>> **" + data["wdesc"] + "** " + data["emote"] + "\n"
        msg += "*Expected high*: " + data["C"]["max"] + " / " + data["F"]["max"] + " **|** *Expected low*: " +data["C"]["min"] + " / " + data["F"]["min"] + "\n"
        msg += "=================**Additional data**=================\n"
        msg += ":sweat_drops: *Humidity:* " + data["humidity"] + " **|** :cyclone: *Wind speed:* " + data["wind"] + " **|** :fog: *Clouds:* " + data["clouds"] + "\n"
        
    else:
        msg = "unknown error"
        
    return msg
        