from discord.ext.commands.core import command
import api
import discord
from discord.ext import tasks, commands
from discord.utils import get
import json

f = open('config.json')
data = json.load(f)
TOKEN = data["token"]
command_prefix = data["prefix"]
#client = discord.Client()
client = commands.Bot(command_prefix = command_prefix)

@client.event
async def on_ready():
    print("Logged in")
    #checknew.start()

@client.command()
async def helpme(ctx):
    embed=discord.Embed(title="—List of commands—")
    embed.add_field(name="!setstream [channel name]", value="Sets the channel for which there will be regular updates of new free games.", inline=False)
    embed.add_field(name="!top [n]", value="Shows the nth free games which is available. Input n as integer between 1-9.", inline=False)
    embed.add_field(name="!newtoday", value="Shows the games which are available for free today.", inline=False)
    embed.add_field(name="!new [number of hours]", value="Shows the games that have become available in amount of hours inputted (an integer only please!)", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def setstream(ctx, channel: discord.TextChannel):
    global stream_channel_id
    stream_channel_id = channel.id
    await ctx.send(f"Set as updates channel! ID {stream_channel_id}")
    stream.start()
            
            
# @client.event
# async def on_message(message):
#     username = str(message.author).split("#")[0]
#     user_message = str(message.content)
#     channel = str(message.channel.name)
#     print(f'{username}: {user_message} ({channel})') 

# @tasks.loop(seconds=3600)
# async def checknew():
#     last = ""
#     channel = client.get_channel(CHANNEL_ID)
    
#     api.topFindings(1)
    
@client.command()
async def top(ctx, arg):
    arg = int(arg)
    responses = []
    try:
        print(isinstance(int(arg), int))
        responses = api.topFindings(arg)
        print(responses)
        response = responses[arg-1]
        print(response[0] + " " + response[1])
        await ctx.send(response[0] + " " + response[1])
    except:
        await ctx.send("Not an integer or not between 1-9!")

@client.command()
async def newtoday(ctx):
    responses = api.newToday()
    if responses == []:
        await ctx.send("No new games today.")
    print(responses)
    for response in responses:
        print(response[0] + " " + response[1])
        await ctx.send(response[0] + " " + response[1])

@client.command()
async def new(ctx, arg):
    responses = api.new(int(arg))
    if responses == []:
        await ctx.send("No new games today.")
    print(responses)
    for response in responses:
        print(response[0] + " " + response[1])
        await ctx.send(response[0] + " " + response[1])


@tasks.loop(minutes=1000)
async def stream():
    print("LOOPED")
    #channel = client.channels.find("name","free-games")
    channel = client.get_channel(stream_channel_id)
    response = api.stream()
    print(response[0] + " " + response[1])
    await channel.send(response[0] + " " + response[1])

client.run(TOKEN)

# api.newFindings()

# api.test()