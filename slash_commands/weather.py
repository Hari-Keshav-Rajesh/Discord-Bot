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
    await interaction.followup.send("Bangalore Current Weather:")
    await interaction.followup.send("Description:%s\nTemperature:%.2fC"%(data['weather'][0]['description'],Cel(data['main']['temp'])))
    await interaction.followup.send("It feels like %.2fC"%(Cel(data['main']['feels_like'])))
    await interaction.followup.send("The pressure is %d hPa"%(data['main']['pressure']))
    await interaction.followup.send("The humidity is at %d percent and wind speed is %f m/s"%(data['main']['humidity'],data['wind']['speed']))