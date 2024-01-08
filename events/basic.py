from client import client

@client.event
async def on_ready():
    print("Kit2 at your service")
    print("---------------------")

@client.event
async def on_member_join(member):
    channel = client.get_channel('935603625605070911')
    await channel.send("AY HOW'S IT GOING")

message_count = 0

@client.event
async def on_message(message):
    global message_count
    message_count += 1
    ctx = await client.get_context(message)

    
    if message_count%500 == 0:
        logData = client.get_command('logData')
        await logData.invoke(ctx)
    
    if message_count%1000 == 0:
        logCommandData = client.get_command('logCommandData')
        await logCommandData.invoke(ctx)
        message_count = 0
    
    await client.process_commands(message)
    