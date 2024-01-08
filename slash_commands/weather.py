from client import client 
import requests
import json

@client.slash_command(name='weather',description='Weather ForeCast')
async def weather(interaction):
    await interaction.response.defer()

    r=requests.get('https://api.openweathermap.org/data/2.5/weather?lat=12.9716&lon=77.5946&appid=e2cf4011212692565243c810f489913f')
    data=r.json()
    def Cel(a):
        C=a-273.15
        return C

    await interaction.followup.send(
        "Bangalore Weather Forecast:\n"
        f"Description:{data['weather'][0]['description']}\n"
        f"Temperature:{Cel(data['main']['temp_min'])}C to {Cel(data['main']['temp_max'])}C\n"
        f"It feels like {Cel(data['main']['feels_like'])}C\n"
        f"The pressure is {data['main']['pressure']} hPa\n"
        f"The humidity is at {data['main']['humidity']} percent and wind speed is {data['wind']['speed']} m/s"
    )