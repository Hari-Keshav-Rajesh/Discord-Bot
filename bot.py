import os
from dotenv import load_dotenv

from client import client


from events.basic import *

from commands.basic import *
from commands.commandData import logCommandData
from commands.messageData import logData
from commands.userTimeData import userTimeData
from commands.myStats import myStats

from slash_commands.bitcoin import bitcoin
from slash_commands.joke import joke
from slash_commands.activity import activity
from slash_commands.trivia import trivia
from slash_commands.weather import weather

load_dotenv()
botToken = os.getenv('botToken')


client.run(botToken)

'''
Main file where all the imports are done and the bot is run
'''
