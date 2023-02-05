import discord
import os
import json
import requests
import random

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def roll_dice():
  dice = random.randint(1,6)
  str(dice)
  return dice

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$commands'):
    await message.channel.send('1. $info - Link to help me page and readme files on github \n2. $commands - List of commands useable with this bot. \n3. $hello - The bot says hello \n4. $inspire - The bot will give you an inspiring message to get you through the day! \n5. $dice - Roll the dice to test your luck. \n6. $rollme - You know what this does...')

  if message.content.startswith('$info'):
    await message.channel.send('This BOT was created by: https://mirae-i.net')

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote) 

  if message.content.startswith('$dice'):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    await message.channel.send('You rolled a: ' + str(dice1) + '\nThe bot rolled a: ' + str(dice2))
    if dice1 > dice2:
      await message.channel.send('\n You win!')
    elif dice1 < dice2:
      await message.channel.send('\n You lose!')
    else:
      await message.channel.send("\n It's a tie. Try again")

  if message.content.startswith('$rollme'):
    await message.channel.send('You asked for it: https://www.youtube.com/watch?v=dQw4w9WgXcQ')

client.run(os.getenv('TOKEN'))