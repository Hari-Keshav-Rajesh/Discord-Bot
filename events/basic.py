from client import client

@client.event
async def on_ready():
    print("Kit2 at your service")
    print("---------------------")

@client.event
async def on_member_join(member):
    channel = client.get_channel('935603625605070911')
    await channel.send("AY HOW'S IT GOING")