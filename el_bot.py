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

async def test(discord_channel): 
    await send_message_to_channel(client, discord_channel, ['Debug: Test Endpoint'])

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
        await hello(client, message.channel, message)
        return

    if 'south africa' in message.content:
        await weather_api_call(client, message.channel, 'Johannesburg')
        return

    if '!weather' in message.content: 
        city_name = message.content.replace('!weather', '')                 
        await weather_api_call(client, message.channel, city_name)
        return

    if message.content == '!commands' or message.content == '!help':
        await print_all_commands_in_channel(client, message.channel, COMMANDS)        
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

client.run(settings.discordToken)