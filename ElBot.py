#El Bot v0 .1
# Started 23 rd January 2019.
# Python 3.6
#
# TODO: Refactor on_message()
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


@client.event
async def on_message(message): 
    commands = Settings.botcommands
    message.content = message.content.lower().strip()

    if message.author == client.user:
        return

    if message.content.startswith('!test'):
        await send_message_to_channel(client, message.channel, ['Debug: getting here'])

    if message.content.startswith('!hello') or message.content.startswith('!hi') or message.content.startswith('!hola'):
        if str(message.author) == Settings.megan:
            msg = 'Dia dhuit ' + str(message.author) + '! Cén chaoi a bhfuil mo chroí agat inniu? \nWho are we suing today?'
        elif str(message.author) == Settings.aaron:
            msg = 'Hola mi amigo' + str(message.author) + '! Why do Canadians store their milk in bags? \nYou are my favourite Canadian ... after Ryan Reynolds :)'
        elif str(message.author) == Settings.ellen:
            msg = 'DEBUG: Finding the name: ' + Settings.ellen + " and in the on_message() function"
        else :
            msg = 'Hola! ' + str(message.author) + ' \nI have no custom greeting for you :( \n' + 'I\'ll work on that but have love heart instead :heart:'            
        await client.send_message(message.channel, msg)

        return

    if 'south africa' in message.content:
        msg = 'Johannesburg, South Africa is currently 18 degrees celsius \n I\'m working on connecting to a real life API but it\'s not ready yet'
        # TODO: Add in an weather API to get the actual value not hard coded.
        await client.send_message(message.channel, msg)
        return

    if message.content == '!weather':        
        msg = 'All weather/ Add a list of string here'
        await client.send_message(message.channel, msg)
        return

    if message.content == '!commands' or message.content == '!help':
        commandsStr = '1. !hello or !hi or !hola \nI\'ll greet you and say hi back. \n\n2. Any mention of \'South Africa\' regardless of capitals\n I\'ll let you know the current temperature \n\n3. !commands or !help\n I\'ll let you know all the commands I can respond to.\n\n 4. !day\n I will respond with the current day of the week becuase why not '#
        commands = ['!hello', '!hi', 'south africa', '!weather', '!commands']
        await client.send_message(message.channel, commandsStr)
        return

    if message.content == '!day':
        strCurrentDay = calendar.day_name[date.today().weekday()]
        await client.send_message(message.channel, 'Today is ' + strCurrentDay + '\n Happy ' + strCurrentDay + '!')
        return

    if message.content.startswith('!') and message.content not in commands:
        await client.send_message(message.channel, 'da fuq! What type of command is that!')
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