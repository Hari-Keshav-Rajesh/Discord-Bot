from client import client 
import requests
import json
import random
import asyncio

#Slash_command to generate a random trivia question and check if user returned answer is right or wrong
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