from client import client
import requests
import json

@client.slash_command(name='activity',description="Random Activity Generator")
async def activity(interaction):
    
    await interaction.response.defer()

    r = requests.get('https://www.boredapi.com/api/activity/')
    data=r.json()

    activities = f"{data['activity']} (requires {data['participants']} participant(s))"
    await interaction.followup.send(f'{activities}')