#El Bot v0 .1
# Started 23 rd January 2019.
# Python 3.6

from discord_commands import send_message_to_channel
from help_functions import print_all_commands_in_channel
from hello_functions import hello
from weather_functions import weather_api_call

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

async def test(message): 
    await send_message_to_channel(message, ['Debug: Test Endpoint'])

async def current_day(message):
    strCurrentDay = calendar.day_name[date.today().weekday()]
    await message.channel.send('Today is ' + strCurrentDay + '\n Happy ' + strCurrentDay + '!')
    return

async def not_a_command(message):
    await message.channel.send('da fuq! What type of command is that!')
    return

@client.event
async def on_message(message): 
    if message.author == client.user:
        return

    message.content = message.content.lower().strip()
    await message.channel.send('DEBUG:')

    if message.content.startswith('!test'):
        await test(message)
        return

    if message.content.startswith('!hello') or message.content.startswith('!hi') or message.content.startswith('!hola'):
        await hello(message)
        return

    if 'south africa' in message.content:
        await weather_api_call(message, 'Johannesburg')
        return

    if '!weather' in message.content: 
        city_name = message.content.replace('!weather', '')                 
        await weather_api_call(message, city_name)
        return

    if message.content == '!commands' or message.content == '!help':
        await print_all_commands_in_channel(message, COMMANDS)        
        return

    if message.content == '!day':
        await current_day(message)
        return

    if message.content.startswith('!') and message.content not in COMMANDS:
        await not_a_command(message)
        return


@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(f'{client.user} has connected to Discord!')
    print(discord.version_info)
    
    game = discord.Game("with the API")
    await client.change_presence(activity=game, status=discord.Status.online)
    # TODO: Get message into a channel to say the bot is online.

client.run(settings.discordToken)