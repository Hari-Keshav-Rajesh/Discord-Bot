from client import client

#command to show the user their personal message count and most common time in the last 1000 messages
@client.command()
async def myStats(ctx):

    await ctx.send("Kit2 is thinking...")
    member = ctx.author
    member_timestamps = []
    message_count = 0

    async for message in ctx.channel.history(limit=1000):
        if message.author == member:
            timeStamp = message.created_at
            member_timestamps.append(timeStamp.strftime("%H:%M"))
            message_count += 1

    most_common_time = max(set(member_timestamps), key=member_timestamps.count)

    await ctx.send(f"You have sent {message_count} messages in the last 1000 messages\n"
                    f"Your most common time is {most_common_time}")
    
