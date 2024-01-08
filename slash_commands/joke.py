from client import client 
import requests
import json

#Slash_command to generate a joke
@client.slash_command(name='joke',description='Randome Joke Generator')
async def joke(interaction):

    await interaction.response.defer()

    r=requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious,political,racist,sexist&type=single')
    data=r.json()

    joke = data['joke']
    await interaction.followup.send(f'{joke}')
