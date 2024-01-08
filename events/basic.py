from client import client

# This event is called when the bot is ready to start being used
@client.event
async def on_ready():
    print("Kit2 at your service")
    print("---------------------")

# This event is called when a member joins the server
@client.event
async def on_member_join(member):
    channel = client.get_channel('935603625605070911')
    await channel.send("AY HOW'S IT GOING")

message_count = 0

# This event is called when a message is sent in the server
@client.event
async def on_message(message):
    global message_count
    message_count += 1
    ctx = await client.get_context(message)

    # Log data every 500 messages
    if message_count%500 == 0:
        logData = client.get_command('logData')
        await logData.invoke(ctx)
    
    # Log command data every 1000 messages
    if message_count%1000 == 0:
        logCommandData = client.get_command('logCommandData')
        await logCommandData.invoke(ctx)
        message_count = 0

    #Process the actual message
    await client.process_commands(message)
    