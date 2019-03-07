#El Bot v0 .1
# Started 23 rd January 2019.
# Python 3.6

from discord_commands import send_message_to_channel
from datetime import date
from discord.ext import commands

import calendar
import configparser
import discord
import json
import requests
import settings

settings.settings_init()

TOKEN = settings.discordToken
client = discord.Client()
bot = commands.Bot(command_prefix='!')

COMMANDS = settings.botcommands
api_key = "b7c78b741c20bb89407567ea32caf294"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

async def test(discord_channel): 
    await send_message_to_channel(client, discord_channel, ['Debug: Test Endpoint'])

async def hello_command(message):
    if str(message.author) == settings.megan:
        msg = 'Dia dhuit ' + str(message.author) + '! Cén chaoi a bhfuil mo chroí agat inniu? \nWho are we suing today?'
    elif str(message.author) == settings.aaron:
        msg = 'Hola mi amigo' + str(message.author) + '! Why do Canadians store their milk in bags? \nYou are my favourite Canadian ... after Ryan Reynolds :)'
    elif str(message.author) == settings.ellen:
        msg = 'DEBUG: Finding the name: ' + settings.ellen + " and in the on_message() function"
    else :
        msg = 'Hola! ' + str(message.author) + ' \nI have no custom greeting for you :( \n' + 'I\'ll work on that but have love heart instead :heart:'            
    await client.send_message(message.channel, msg)

async def south_africa_Weather(channel):
    msg = 'Johannesburg, South Africa is currently 18 degrees celsius \n I\'m working on connecting to a real life API but it\'s not ready yet'
    # TODO: Add in an weather API to get the actual value not hard coded.
    await client.send_message(channel, msg)
    return

async def weather(channel, city):
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
    return


async def all_bot_commands(channel):
    commandsStr = '1. !hello or !hi or !hola \nI\'ll greet you and say hi back. \n\n2. Any mention of \'South Africa\' regardless of capitals\n I\'ll let you know the current temperature \n\n3. !commands or !help\n I\'ll let you know all the commands I can respond to.\n\n 4. !day\n I will respond with the current day of the week becuase why not '#
    await client.send_message(channel, commandsStr)
    return

async def current_day(channel):
    strCurrentDay = calendar.day_name[date.today().weekday()]
    await client.send_message(channel, 'Today is ' + strCurrentDay + '\n Happy ' + strCurrentDay + '!')
    return

async def not_a_command(channel):
    await client.send_message(channel, 'da fuq! What type of command is that!')
    return

@client.event
async def on_message(message): 
    if message.author == client.user:
        return

    message.content = message.content.lower().strip()

    if message.content.startswith('!test'):
        await test(message.channel)
        return

    if message.content.startswith('!hello') or message.content.startswith('!hi') or message.content.startswith('!hola'):
        await hello_command(message)
        return

    if 'south africa' in message.content:
        await weather(message.channel, 'Johannesburg')
        return

    if '!weather' in message.content: 
        city_name = message.content.replace('!weather', '')         
        await weather(message.channel, city_name)
        return

    if message.content == '!commands' or message.content == '!help':
        await all_bot_commands(message.channel)
        return

    if message.content == '!day':
        await current_day(message.channel)
        return

    if message.content.startswith('!') and message.content not in COMMANDS:
        await not_a_command(message.channel)
        return


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game = discord.Game(name = "with humans"))
    # TODO: Get message into a channel to say the bot is online.

client.run(TOKEN)