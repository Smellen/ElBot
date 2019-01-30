# El Bot v0 .1
# 29th January 2019
# Functions related to El bot response to Hello
import discord
from DiscordCommands import send_message_to_channel

TOKEN = 'NTM1NTY4NTYxMDkyMDM0NTYw.DyKDqw.UrFBjjWZTyf8jGuc6YmE0z92R2E'
client = discord.Client()

async def hello(message):
    print('here' + str(message.channel))
    msg = 'Debug - else statement. HelloFunctions.py'
    await client.send_message(message.channel, msg)

# TODO: Add a function per user to return their custom messages.
client.run(TOKEN)