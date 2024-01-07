from client import client
from db import connection


@client.command()
async def logCommandData(ctx):

    await ctx.send("Logging Command Data....")

    commands_counter={"!hello":0,"!userTimeData":0,"!goodbot":0,"!shutdown":0}

    async for message in ctx.channel.history(limit=1000):
            if message.content in commands_counter:
                commands_counter[message.content] += 1
    
    insert_query = "INSERT INTO commands (hello, userTimeData,goodbot,shutdown) VALUES (%s, %s,%s,%s)"

    values = tuple(commands_counter[key] for key in ["!hello", "!userTimeData", "!goodbot", "!shutdown"])

    with connection.cursor() as cursor:
        cursor.execute(insert_query, values)
        connection.commit()
     
    await ctx.send("Logging Complete")