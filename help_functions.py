# El Bot v0 .1
# 21st August 2019
# Functions related to help function
import discord

async def print_all_commands_in_channel(message, listOfCommands):
    allCommands = ""

    for cmd in listOfCommands:
        allCommands = allCommands + cmd + "\n"
 
    await message.channel.send(allCommands)