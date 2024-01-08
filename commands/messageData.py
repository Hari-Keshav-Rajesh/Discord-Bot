from client import client
from db import connection

import requests
import json
import pandas as pd


@client.command()
async def logData(ctx):
    await ctx.send("Logging Data....")
    time = []
    date = []
    async for message in ctx.channel.history(limit=500):
        timeStamp = message.created_at
        time.append(timeStamp.strftime("%H:%M"))
        date.append(timeStamp.strftime("%Y-%m-%d"))

    guild = ctx.guild

    async def message_count(ctx, user):
        count = 0
        async for message in ctx.channel.history(limit=500):
            if message.author == user:
                count += 1
        return count

    member_data = []

    async def update_members():
        for member in guild.members:
            message_num = await message_count(ctx, member)
            member_data.append(
                {
                    "ID": member.id,
                    "Username": member.name,
                    "JoinDate": member.joined_at.strftime("%Y-%m-%d %H:%M:%S"),
                    "MessageCount": message_num,
                }
            )

    await update_members()

    insert_query = "INSERT INTO activity (time_col, date_col,max_name,max_count,min_name,min_count) VALUES (%s, %s,%s,%s,%s,%s)"

    timeStamp_df = pd.DataFrame({"date": date, "time": time})
    time_mode = list(timeStamp_df.time.mode())
    date_mode = list(timeStamp_df.date.mode())

    members_df = pd.DataFrame(member_data)
    member_high_idx = members_df.MessageCount.idxmax()
    member_high_count = members_df.iloc[member_high_idx]["MessageCount"]
    member_high_name = members_df.iloc[member_high_idx]["Username"]

    member_low_idx = members_df.MessageCount.idxmin()
    member_low_count = members_df.iloc[member_low_idx]["MessageCount"]
    member_low_name = members_df.iloc[member_low_idx]["Username"]

    with connection.cursor() as cursor:
        cursor.execute(
            insert_query,
            (
                time_mode[0],
                date_mode[0],
                member_high_name,
                str(member_high_count),
                member_low_name,
                str(member_low_count),
            ),
        )

    connection.commit()

    await ctx.send("Logging Complete")
