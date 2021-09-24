import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import openai
load_dotenv()

#API tokens
openai.api_key = os.getenv('OPENAI_API_KEY')
token = os.getenv('TOK')

#Inits
intents = discord.Intents.all()
engines = openai.Engine.list()


client = commands.Bot(case_insensitive=True, command_prefix='.j ', intents=intents)

#Bot is ready
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle)

@client.command()
async def test(ctx, *, line):
    completion = openai.Completion.create(engine="ada", prompt=line)
    await ctx.send(line + completion.choices[0].text)

client.run(token)
