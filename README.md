# ElBot
A custom discord bot.

# Local setup
## Pre requisites
- python 3
- pip
- pip module requests
- pip module discord
- discord API token

**el_bot.py**

This is the main file that starts the connection to discord.

**hello_functions.py**

Work in progress.

**settings.py**

This is where the config files are read and values are stored into global variables accessed from other parts of the bot.

**discord_commands.py**

Work in progress

**config.json**

Values that have the potential to change to reduce changing any py files. These values will be stored in global variables for the moment.

All Discord bot commands:

**Command** | **Description** |
--- | --- | 
!hello  | The bot will say hello to the user with a custom message. | 
!weather !city | The bot will make a call to a weather API and pull back the temperature and brief description. |
!day | Will return the current day. |
!test | A test command that is used for debugging. |
!commands or !help | Lists all available commands and a brief description of each. |

# TODO: 
* Add in randomising of response messages.
* Remove all hardcoded values, they should be read from settings/configs.
* Proper README
* Update the !help command with a full list. Read from config not hard coded.
* Use Python coding standards.
* Unit tests? 
