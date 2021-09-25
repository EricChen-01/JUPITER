import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import requests

load_dotenv()

#API tokens
deepai_key = os.getenv("DEEPAI_API_KEY")
token = os.getenv('TOK')

#Inits
intents = discord.Intents.all()

client = commands.Bot(case_insensitive=True, command_prefix='.j ', intents=intents)

def deepai_complete(prompt: str):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': prompt,
        },
        headers={'api-key': deepai_key}
    )
    return r

#Bot is ready
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle)

##############################Code starts here################################

#Completion API code. AKA the main thing we will be working on

#Parameters:
#ctx = contex <-- no need to worry about what this is.
#line: the actual line of text user inputs

#outputs:
#ctx.send <-- sends to discord chat
@client.command()
async def test(ctx, *, line):

    completion = deepai_complete(line)
    await ctx.send(completion.json()['output'])

client.run(token)
