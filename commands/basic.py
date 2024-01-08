from client import client

@client.command()
async def hello(ctx):
    await ctx.send("HI, I'm Kit2")


@client.command()
async def goodbot(ctx):
    await ctx.send("Thanks a ton")

@client.command()
async def shutdown(ctx):
    if ctx.author.id==756436088515723324:
        await ctx.send("Shut Down Initiated")
        await client.close()
    else:
        await ctx.send("You don't have permission to initiate shut down")