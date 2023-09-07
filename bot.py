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
async def shutdown(ctx):
    if ctx.author.id==756436088515723324:
        await ctx.send("Shut Down Initiated")
        await client.close()
    else:
        await ctx.send("You don't have permission to initiate shut down")


@client.command()
async def userData(ctx):
    guild = ctx.guild

    
    
    async def message_count(ctx, user):
        count = 0
        async for message in ctx.channel.history(limit=1000):
            if message.author == user:
                count += 1
        return count

    member_data = []
    async def update_members():
        
                
        for member in guild.members:
            message_num = await message_count(ctx,member)
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

        member_low_idx = members_df.MessageCount.idxmin()
        member_low_count = members_df.iloc[member_low_idx]['MessageCount']
        member_low_name  = members_df.iloc[member_low_idx]['Username']

        await ctx.send(f"Maximum activity over past 1000 messages by user: {member_high_name}\nSent {member_high_count} messages.\n")

        await ctx.send(f"Minimum activity over past 1000 messages by user: {member_low_name}\nSent {member_low_count} messages.\n")

  


    await update_members()
        

@client.command()
async def commandData(ctx):

    commands_counter={"!hello":0,"!userData":0,"!commandData":0,"!goodbot":0,"!shutdown":0,"!timeData":0}

    async for message in ctx.channel.history(limit=1000):
            if message.content in commands_counter:
                commands_counter[message.content] += 1
    
    await ctx.send("The number of times each command was used in the past 1000 messages is:\n")

    for key in commands_counter:
            await ctx.send(f"{key} has been used {commands_counter[key]} times\n") 

@client.command()
async def timeData(ctx):
    time=[]
    date=[]
    async for message in ctx.channel.history(limit=1000):
            timeStamp = message.created_at
            time.append(timeStamp.strftime("%H:%M"))
            date.append(timeStamp.strftime("%Y-%m-%d"))

    timeStamp_df = pd.DataFrame({"date":date,"time":time})

    time_mode = timeStamp_df.time.mode()
    date_mode = timeStamp_df.date.mode()

    await ctx.send(f"Most active session time(s) over the past 1000 messages were at:\n")
    for i in time_mode:
        await ctx.send(f"{i}\n")

    await ctx.send(f"Most active date(s) over the past 1000 messages are:\n")
    for i in date_mode:
        await ctx.send(f"{i}\n")


@client.command()
async def userTimeData(ctx):
    guild = ctx.guild
    member_names = []
    member_time = []

    for member in guild.members:
        member_timestamps = []

        async for message in ctx.channel.history(limit=1000):
            if message.author == member:
                timeStamp = message.created_at
                member_timestamps.append(timeStamp.strftime("%H:%M"))

        
        member_names.append(member.name)
        most_common_time = max(set(member_timestamps), key=member_timestamps.count)
        member_time.append(most_common_time)

    member_df = pd.DataFrame({'Username': member_names, 'Time': member_time})

    member_group = member_df.groupby('Username').Time.apply(lambda x: x.mode().iloc[0]).reset_index()

    await ctx.send("The times at which users are most active are\n")
    for index, row in member_group.iterrows():
        username = row['Username']
        time = row['Time']
        await ctx.send(f"Username: {username}, Time: {time}")








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



@client.slash_command(name='weather',description='Weather ForeCast')
async def weather(interaction):
    await interaction.response.defer()

    r=requests.get('https://api.openweathermap.org/data/2.5/weather?lat=12.9716&lon=77.5946&appid=e2cf4011212692565243c810f489913f')
    data=r.json()
    def Cel(a):
        C=a-273.15
        return C
    await interaction.followup.send("Bangalore Current Weather:")
    await interaction.followup.send("Description:%s\nTemperature:%.2fC"%(data['weather'][0]['description'],Cel(data['main']['temp'])))
    await interaction.followup.send("It feels like %.2fC"%(Cel(data['main']['feels_like'])))
    await interaction.followup.send("The pressure is %d hPa"%(data['main']['pressure']))
    await interaction.followup.send("The humidity is at %d percent and wind speed is %f m/s"%(data['main']['humidity'],data['wind']['speed']))



@client.slash_command(name='bitcoin',description='Latest BitCoin Values')
async def bitcoin(interaction):

    await interaction.response.defer()

    r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data=r.json()
    
    await interaction.followup.send(f"The current time is {data['time']['updateduk']}")
    await interaction.followup.send(data['disclaimer'])
    await interaction.followup.send("The current Bitcoin rate of 1%s(%s) is %s"%(data['bpi']['USD']['code'],data['bpi']['USD']['description'],data['bpi']['USD']['rate']))
    await interaction.followup.send("The current Bitcoin rate of 1%s(%s) is %s"%(data['bpi']['GBP']['code'],data['bpi']['GBP']['description'],data['bpi']['GBP']['rate']))
    await interaction.followup.send("The current Bitcoin rate of 1%s(%s) is %s"%(data['bpi']['EUR']['code'],data['bpi']['EUR']['description'],data['bpi']['EUR']['rate']))



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