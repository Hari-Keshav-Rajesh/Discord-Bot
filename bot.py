from client import client

from apikeys import botToken


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

client.run(botToken)
