import disnake
from disnake.ext import commands

import requests
import json
import asyncio
import random
import pandas as pd

from apikeys import *




intents = disnake.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='!',intents=intents)

#EVENTS

@client.event
async def on_ready():
    print("Kit2 at your service")
    print("---------------------")

@client.event
async def on_member_join(member):
    channel = client.get_channel('935603625605070911')
    await channel.send("AY HOW'S IT GOING")







#COMMANDS

@client.command()
async def hello(ctx):
    await ctx.send("HI, I'm Kit2")


@client.command()
async def goodbot(ctx):
    await ctx.send("Thanks a ton")
    r=requests.get('https://complimentr.com/api')
    data=r.json()
    await ctx.send(data['compliment'])


@client.command()
async def data(ctx):
    guild = ctx.guild

    async def message_count(user):
        count = 0
        async for message in ctx.channel.history(limit=1000):
            if message.author == user:
                count += 1
        return count

    member_data = []
    async def update_members():
        for member in guild.members:
            message_num = await message_count(member)
            member_data.append({
                'ID': member.id,
                'Username': member.name,
                'JoinDate': member.joined_at.strftime('%Y-%m-%d %H:%M:%S'),
                'MessageCount': message_num
            })

        members_df = pd.DataFrame(member_data)

        member_high_idx = members_df.MessageCount.idxmax()
        member_high_count = members_df.iloc[member_high_idx]['MessageCount']
        member_high_name  = members_df.iloc[member_high_idx]['Username']
        await ctx.send(f"Maximum activity over past 1000 messages by user: {member_high_name}\nSent {member_high_count} messages.")



    await update_members()
        
    




#SLASH COMMANDS


@client.slash_command(name='activity',description="Random Activity Generator")
async def activity(interaction):
    
    await interaction.response.defer()

    r = requests.get('https://www.boredapi.com/api/activity/')
    data=r.json()

    activities = f"{data['activity']} (requires {data['participants']} participant(s))"
    await interaction.followup.send(f'{activities}')


@client.slash_command(name='joke',description='Randome Joke Generator')
async def joke(interaction):

    await interaction.response.defer()

    r=requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious,political,racist,sexist&type=single')
    data=r.json()

    joke = data['joke']
    await interaction.followup.send(f'{joke}')

@client.slash_command(name='trivia',description="Random Trivia Question")
async def trivia(interaction):
    
    await interaction.response.defer()

    r = requests.get('https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple')
    data=r.json()

    question = data['results'][0]['question']
    answer_list = (data['results'][0]['correct_answer']).split("delimiter")  + data['results'][0]['incorrect_answers']
    random.shuffle(answer_list)

    await interaction.followup.send(f"{question} \n The options are {answer_list[0]}, {answer_list[1]}, {answer_list[2]}, {answer_list[3]} \n Enter your answer")
    
    try:
        answer = await client.wait_for("message",timeout=30)
    except:
        asyncio.TimeoutError(f"The correct answer is {data['results'][0]['correct_answer']}")
    
    if(answer.content==(data['results'][0]['correct_answer']).strip()):
        await interaction.followup.send("That is the CORRECT ANSWER!!!")
    else:
        await interaction.followup.send(f"Oops!That's incorrect! The correct answer is {data['results'][0]['correct_answer']}")
    















client.run(botToken)