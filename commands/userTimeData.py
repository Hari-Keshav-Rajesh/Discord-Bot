from client import client
import pandas as pd

@client.command()
async def userTimeData(ctx):
    guild = ctx.guild
    member_names = []
    member_time = []

    for member in guild.members:
        member_timestamps = []

        async for message in ctx.channel.history(limit=1000):
            if message.author == member:
                timeStamp = message.created_at
                member_timestamps.append(timeStamp.strftime("%H:%M"))

        
        member_names.append(member.name)
        most_common_time = max(set(member_timestamps), key=member_timestamps.count)
        member_time.append(most_common_time)

    member_df = pd.DataFrame({'Username': member_names, 'Time': member_time})

    member_group = member_df.groupby('Username').Time.apply(lambda x: x.mode().iloc[0]).reset_index()

    await ctx.send("The times at which users are most active are\n")
    for index, row in member_group.iterrows():
        username = row['Username']
        time = row['Time']
        await ctx.send(f"Username: {username}, Time: {time}")