# El Bot v0 .1
# 29th January 2019
# Functions related to El bot for sending commands to Discord.
import discord

async def send_message_to_channel(message, listOfMessages):

    print('Channel name ' + message.channel.name)

    for msg in listOfMessages:
        print('message: ' + msg)
        await message.channel.send(msg)
