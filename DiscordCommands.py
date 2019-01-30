# El Bot v0 .1
# 29th January 2019
# Functions related to El bot for sending commands to Discord.
import discord

async def send_message_to_channel(client, channel, listOfMessages):

    print('Channel name ' + channel.name)

    for msg in listOfMessages:
        print('message: ' + msg)
        await client.send_message(channel, msg)

