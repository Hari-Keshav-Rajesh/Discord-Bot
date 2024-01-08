from client import client

#Command used to greet the bot
@client.command()
async def hello(ctx):
    await ctx.send("HI, I'm Kit2")

#Command to praise the bot
@client.command()
async def goodbot(ctx):
    await ctx.send("Thanks a ton")

#Command to shut down bot activities (only usable by the bot owner)
@client.command()
async def shutdown(ctx):
    if ctx.author.id==756436088515723324:
        await ctx.send("Shut Down Initiated")
        await client.close()
    else:
        await ctx.send("You don't have permission to initiate shut down")