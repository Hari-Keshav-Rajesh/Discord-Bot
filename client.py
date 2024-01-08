import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='!',intents=intents)

'''
File to declare the client and the intents
'''