#El Bot v0 .1
# Started 23 rd January 2019.
# Python 3.6
#
# TODO: 
# Add in randomising of response messages.
# Remove all hardcoded values, they should be read from settings/configs.
# Extract send_message() into a common function
# Unit tests? 

from DiscordCommands import send_message_to_channel
from datetime import date
import calendar
import configparser
import discord
import Settings

Settings.settings_init()

TOKEN = Settings.discordToken
client = discord.Client()
COMMANDS = Settings.botcommands

async def test(discord_channel):
    await send_message_to_channel(client, discord_channel, ['Debug: getting here'])

async def hello_command(message):
    if str(message.author) == Settings.megan:
        msg = 'Dia dhuit ' + str(message.author) + '! Cén chaoi a bhfuil mo chroí agat inniu? \nWho are we suing today?'
    elif str(message.author) == Settings.aaron:
        msg = 'Hola mi amigo' + str(message.author) + '! Why do Canadians store their milk in bags? \nYou are my favourite Canadian ... after Ryan Reynolds :)'
    elif str(message.author) == Settings.ellen:
        msg = 'DEBUG: Finding the name: ' + Settings.ellen + " and in the on_message() function"
    else :
        msg = 'Hola! ' + str(message.author) + ' \nI have no custom greeting for you :( \n' + 'I\'ll work on that but have love heart instead :heart:'            
    await client.send_message(message.channel, msg)

async def south_africa_Weather(channel):
    msg = 'Johannesburg, South Africa is currently 18 degrees celsius \n I\'m working on connecting to a real life API but it\'s not ready yet'
    # TODO: Add in an weather API to get the actual value not hard coded.
    await client.send_message(channel, msg)
    return

async def weather(channel):
    msg = 'All weather/ Add a list of string here'
    await client.send_message(channel, msg)
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

    if message.content.startswith('!hello') or message.content.startswith('!hi') or message.content.startswith('!hola'):
        await hello_command(message)
        return

    if 'south africa' in message.content:
        await south_africa_Weather(message.channel)

    if message.content == '!weather':        
        await weather(message.channel)

    if message.content == '!commands' or message.content == '!help':
        await all_bot_commands(message.channel)

    if message.content == '!day':
        await current_day(message.channel)

    if message.content.startswith('!') and message.content not in COMMANDS:
        await not_a_command(message.channel)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game = discord.Game(name = "with humans"))
    # TODO: Get message into a channel to say the bot is online.

client.run(TOKEN)