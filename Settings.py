# 30th January 
# Settings file that reads values from the config.
import json

megan = ''
ellen = ''
arissa = ''
aaron = ''
kristin = ''

botcommands = []

discordToken = ''

def get_dict_keys(discordNames, val):
        return [k for k in discordNames.keys() if discordNames[k] == val][0]


def getUserNames(discordUsernames):
    global megan
    global ellen
    global arissa
    global aaron
    global kristin

    megan = get_dict_keys(discordUsernames, 'Megan')
    ellen = get_dict_keys(discordUsernames, 'Ellen')
    aaron = get_dict_keys(discordUsernames, 'Aaron')
    arissa = get_dict_keys(discordUsernames, 'Arissa')
    kristin = get_dict_keys(discordUsernames, 'Kristin')


def getCommands(botcommandsPassedIn):
        global botcommands
        botcommands = botcommandsPassedIn
        # TODO: In the JSON add the definition for the command to be stored there as well.    
    
def settings_init():
    with open('config.json', 'r') as f:
        config = json.load(f)

    discordUsernames = config['USERNAMES']
    botcommands = config['COMMANDS']
    getUserNames(discordUsernames)
    getCommands(botcommands)

    global discordToken
    discordToken = 'NTM1NTY4NTYxMDkyMDM0NTYw.DyKDqw.UrFBjjWZTyf8jGuc6YmE0z92R2E'

print("About to start")
settings_init()