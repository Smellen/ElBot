#El Bot v0 .1
# 21st August 2019
# Python 3.6

from discord_commands import send_message_to_channel
from datetime import date
import requests

api_key = "b7c78b741c20bb89407567ea32caf294"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

async def weather_api_call(client, channel, city):
    complete_url = base_url + "appid=" + api_key + "&q=" + str(city) 
    response = requests.get(complete_url) 
    weather_results = response.json() 
    msg = ''
    
    try:
        y = weather_results["main"] 
        current_temperature = y["temp"] 
        z = weather_results["weather"] 
        weather_description = z[0]["description"] 
        degrees = (int(current_temperature)) -  273.15 
        farenheit = degrees * (9/5) + 32
        str(current_temperature)
        msg = 'API data from: api.openweathermap.org\n\nCity: ' + str(city) + '\nCurrent temperature: \n\t' + str(round(degrees, 2)) + '°C\n\t' + str(round(farenheit, 2))+ '°F' + '\nBrief weather description: ' + str(weather_description)

    except:
        msg = 'Something went wrong! Try again only city names and countries are accepted'

    await send_message_to_channel(client, channel, [msg])