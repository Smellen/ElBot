# El Bot v0 .1
# 29th January 2019
# Functions related to El bot response to Hello
import discord
from discord_commands import send_message_to_channel
import settings

settings.settings_init()

async def hello(message):
    print('here' + str(message.channel.name))
    if str(message.author) == settings.megan:
        msg = 'Dia dhuit ' + str(message.author) + '! Cén chaoi a bhfuil mo chroí agat inniu? \nWho are we suing today?'
    elif str(message.author) == settings.aaron:
        msg = 'Hola mi amigo' + str(message.author) + '! Why do Canadians store their milk in bags? \nYou are my favourite Canadian ... after Ryan Reynolds :)'
    elif str(message.author) == settings.ellen:
        msg = 'DEBUG: Finding the name: ' + settings.ellen + " and in the on_message() function"
    else :
        msg = 'Hola! ' + str(message.author) + ' \nI have no custom greeting for you :( \n' + 'I\'ll work on that but have love heart instead :heart:'            
    await message.channel.send(msg)