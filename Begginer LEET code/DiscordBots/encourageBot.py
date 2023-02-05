# Import the discord package and run the file so replit can download the necessary dependencies.

import discord
import os
import requests
import json
import random
from replit import db

# Discord bot runs almost entirely off of events. That means that the bot waits for some message from the user that it will then respond to.

# Discord is an asynchronous library which means that it is a function that runs on callbacks. A callback is a function that is called when something else happens.

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there!",
  "You got this!"
]

if "responding" not in db.keys():
  db["responding"] = True

# This event is going to be called as soon as the bot is ready to be used.

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

@client.event
async def on_ready(): # ready event
  print('We have logged in as {0.user}'.format(client)) 

# it will print the user name that is lodded in as

# next we will code the bot to reply to messages when they are recieved. However we don't want the bot to reply to a message if it is from itself.

@client.event # same client event
async def on_message(message): # event will trigger upon recieving a message
  if message.author == client.user: # check if the message is from itself
    return # return nothing

  msg = message.content

  if message.content.startswith('$hello'): # event will trigger if a user sends this
    await message.channel.send('Hello!') # bot will reply

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$commands"):
    await message.channel.send("Here is a list of commands \n$new = Adds a new encouraging message \n$del = delete an encouraging message from the DB \n$list = get a list of messages stored in the DB. \n$help = a breif description of this bots usage ")

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if message.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on!")

    else:
      db["responding"] = False
      await message.channel.send("Responding is off!")
    

client.run(os.getenv('TOKEN')) # run the bot using the necessary TOKEN