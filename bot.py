# bot.py
import os
import random
import requests
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()
#
# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#
# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )
#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]
#
#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)
#
#     help_response = 'How can I help you?'
#
#     if message.content == 'help':
#         await message.channel.send(help_response)
#
#
# client.run(TOKEN)

bot = commands.Bot(command_prefix='!')

#Bot command simulating picking a card
@bot.command(name='pick_card', help='Simulates picking a card.')
async def pick(ctx):
    #Range of possible cards
    cards = [
        2,3,4,5,6,7,8,9,10, "Jack", "Queen", "King", "Ace"
    ]

    #Range of possible suits
    suit = [
        "hearts", "diamonds", "spades", "clubs"
    ]

    #Randomize both variables
    response = str(random.choice(cards))
    response2 = random.choice(suit)

    #Concatonate response
    await ctx.send(response + " of " + response2)


@bot.command(name='office', help='Responds with a random quote from the Office')
async def office(ctx):
    office_quotes = [
        'Well, well, well, how the turntables.',
        'Thats what she said.',
        'Mo money, Mo problems.',
    ]

    response = random.choice(office_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

## Calling weather data using API

# API KEY
API_key = "b5882f16d079cdc20d9701594ef13525"

# This stores the url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#Command returning weather for given city name
@bot.command(name='weather', help='Reveals weather of chosen city.')
async def pick(ctx, city_name: str):

    # This is final url. This is concatenation of base_url, API_key and city_nmae
    Final_url = base_url + "appid=" + API_key + "&q=" + city_name

    # this variable contain the JSON data which the API returns
    weather_data = requests.get(Final_url).json()

    # Concatonates strings together
    await ctx.send("\nCurrent Weather Data Of " + city_name +":\n" + str(weather_data))

bot.run(TOKEN)
