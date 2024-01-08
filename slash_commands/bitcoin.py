from client import client 
import requests
import json

#Slash_command to show current bitcoin prices in USD, GBP and EUR
@client.slash_command(name='bitcoin',description='Latest BitCoin Values')
async def bitcoin(interaction):

    await interaction.response.defer()

    r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data=r.json()
    
    await interaction.followup.send(
    f"The current time is {data['time']['updateduk']}\n"
    f"{data['disclaimer']}\n"
    f"The current Bitcoin rate of 1{data['bpi']['USD']['code']}({data['bpi']['USD']['description']}) is {data['bpi']['USD']['rate']}\n"
    f"The current Bitcoin rate of 1{data['bpi']['GBP']['code']}({data['bpi']['GBP']['description']}) is {data['bpi']['GBP']['rate']}\n"
    f"The current Bitcoin rate of 1{data['bpi']['EUR']['code']}({data['bpi']['EUR']['description']}) is {data['bpi']['EUR']['rate']}"
    )
