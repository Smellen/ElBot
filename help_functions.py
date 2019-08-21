# El Bot v0 .1
# 21st August 2019
# Functions related to help function
import discord

async def print_all_commands_in_channel(client, channel, listOfCommands):
    allCommands = ""

    for cmd in listOfCommands:
        allCommands = allCommands + cmd + "\n"
 
    await client.send_message(channel, allCommands)