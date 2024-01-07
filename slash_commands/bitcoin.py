from client import client 
import requests
import json

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