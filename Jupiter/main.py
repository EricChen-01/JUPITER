import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import openai
import requests

load_dotenv()

#API tokens
openai.api_key = os.getenv('OPENAI_API_KEY')
deepai_key = os.getenv("DEEPAI_API_KEY")
token = os.getenv('TOK')

#Inits
intents = discord.Intents.all()
engines = openai.Engine.list()
ai_bot = GenericAssistant('intents.json')
ai_bot.train_model()
ai_bot.save_model()

client = commands.Bot(case_insensitive=True, command_prefix='.j ', intents=intents)

#DeepAI helper functions
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
async def starter(ctx, *, line):
    completion = openai.Completion.create(engine="ada", prompt=line)
    await ctx.send(completion.choices[0].text)

@client.command()
async def starter2(ctx, *, line):
    completion = deepai_complete(line)
    await ctx.send(completion.json()['output'])

@client.command()
async def ai(ctx, context):
    response = ai_bot.request(context)
    await ctx.send(response)

@client.command()
async def outline(ctx, *, topic):
    prompt = f'Create an outline for an essay about {topic}:\n\nI: Introduction'
    response = openai.Completion.create(
        engine="ada",
        prompt=prompt,
        temperature=0.7,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0)
    await ctx.send('I: Introduction' + response.choices[0].text)

client.run(token)
