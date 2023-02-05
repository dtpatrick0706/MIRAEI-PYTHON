# Step 1

import discord
import os
import random
from replit import db

# Step 2

userChips = []
client = discord.Client()

if "responding" not in db.keys():
	db["responding"] = True

# Step 3

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

# Step 4

rNum1 = random.randint(1,45)
rNum2 = random.randint(1,45)
rNum3 = random.randint(1,45)
rNum4 = random.randint(1,45)
rNum5 = random.randint(1,45)
rNum6 = random.randint(1,45)

print("Lottery Winning Numbers =", rNum1, rNum2, rNum3, rNum4, rNum5, rNum6)

print("\nInstruction to person controlling this bot \nThis Arcade Bot is used to gamble peoples currency called 'chips'. \nMost of them are related to luck, you cannot use any skill related commands here. \nLottery Numbers are listed above. \nTo use this bot, simply run the command... Wait, if you didn't run the code how are you \nreading this?\n")

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('>commands'):
		await message.channel.send(">commands -> Check Commands")
		await message.channel.send(">prefix -> Check Prefix")
		await message.channel.send(">checkChips -> Check Chips")
		await message.channel.send(">chipspls -> Get Chips")
		await message.channel.send(">rollTen -> Roll A Number From 1 To 10 And Test Your Luck")
		await message.channel.send(">rollFifty -> Roll A Number From 1 To 50 And Test Your Luck")
		await message.channel.send(">rollHundred -> Roll A Number From 1 To 100 And Test Your Luck")
	
	if message.content.startswith('>prefix'):
		await message.channel.send("Prefix : >")

	if message.content.startswith('>chipspls'):
		await message.channel.send("Here, have 100 Chips!")
	
	if message.content.startswith('>checkChips'):
		await message.channel.send("Your Chips : n")

	if message.content.startswith('!time'):
		await message.channel.send("hahabad noah")

	if message.content.startswith('>blackJack'):
   
		bjCards = [
			"A",
			"K",
			"Q",
			"J",
			10,
			9,
			8,
	    7,
			6,
			5,
			4,
			3,
			2
		]

		card1 = random.choice(bjCards)
		card2 = random.choice(bjCards)
		card3 = random.choice(bjCards)
		card1r = random.choice(bjCards)
		card2r = random.choice(bjCards)
		card3r = random.choice(bjCards)
		toggleIt = 0
		toggleItr = 0

		card11 = card1
		card22 = card2
		card33 = card3
		card44 = 0
		card55 = 0
		card66 = 0

		card11r = card1r
		card22r = card2r
		card33r = card3r
		card44r = 0
		card55r = 0
		card66r = 0

		if card1 == 'K':
			card11 = 10
			toggleIt = 1
		if card2 == 'K':
			card22 = 10
			toggleIt = 2
		if card3 == 'K':
			card33 = 10
			toggleIt = 4			
		if card1 == 'Q':
			card11 = 10
			toggleIt = 1
		if card2 == 'Q':
			card22 = 10
			toggleIt = 2
		if card3 == 'Q':
			card33 = 10
			toggleIt = 4	
		if card1 == 'J':
			card11 = 10
			toggleIt = 1
		if card2 == 'J':
			card22 = 10
			toggleIt = 2
		if card3 == 'J':
			card33 = 10
			toggleIt = 4	
		if card1 == 'A':
			card44 = 11
			toggleIt = 1
		if card2 == 'A':
			card55 = 11
			toggleIt = 2
		if card3 == 'A':
			card66 = 11
			toggleIt = 4



		if card1 == 'K' and card2 == 'K':
			toggleIt = 3
		if card1 == 'K' and card2 == 'Q':
			toggleIt = 3
		if card1 == 'K' and card2 == 'J':
			toggleIt = 3
		if card1 == 'Q' and card2 == 'K':
			toggleIt = 3
		if card1 == 'Q' and card2 == 'Q':
			toggleIt = 3
		if card1 == 'Q' and card2 == 'J':
			toggleIt = 3
		if card1 == 'J' and card2 == 'K':
			toggleIt = 3
		if card1 == 'J' and card2 == 'Q':
			toggleIt = 3
		if card1 == 'J' and card2 == 'J':
			toggleIt = 3
		if card1 == 'A' and card2 == 'K':
			toggleIt = 3
		if card1 == 'A' and card2 == 'Q':
			toggleIt = 3
		if card1 == 'A' and card2 == 'J':
			toggleIt = 3

		if card1 == 'K' and card3 == 'K':
			toggleIt = 3
		if card1 == 'K' and card3 == 'Q':
			toggleIt = 3
		if card1 == 'K' and card3 == 'J':
			toggleIt = 3
		if card1 == 'Q' and card3 == 'K':
			toggleIt = 3
		if card1 == 'Q' and card3 == 'Q':
			toggleIt = 3
		if card1 == 'Q' and card3 == 'J':
			toggleIt = 3
		if card1 == 'J' and card3 == 'K':
			toggleIt = 3
		if card1 == 'J' and card3 == 'Q':
			toggleIt = 3
		if card1 == 'J' and card3 == 'J':
			toggleIt = 3
		if card1 == 'A' and card3 == 'K':
			toggleIt = 3
		if card1 == 'A' and card3 == 'Q':
			toggleIt = 3
		if card1 == 'A' and card3 == 'J':
			toggleIt = 3

		if card3 == 'K' and card2 == 'K':
			toggleIt = 3
		if card3 == 'K' and card2 == 'Q':
			toggleIt = 3
		if card3 == 'K' and card2 == 'J':
			toggleIt = 3
		if card3 == 'Q' and card2 == 'K':
			toggleIt = 3
		if card3 == 'Q' and card2 == 'Q':
			toggleIt = 3
		if card3 == 'Q' and card2 == 'J':
			toggleIt = 3
		if card3 == 'J' and card2 == 'K':
			toggleIt = 3
		if card3 == 'J' and card2 == 'Q':
			toggleIt = 3
		if card3 == 'J' and card2 == 'J':
			toggleIt = 3
		if card3 == 'A' and card2 == 'K':
			toggleIt = 3
		if card3 == 'A' and card2 == 'Q':
			toggleIt = 3
		if card3 == 'A' and card2 == 'J':
			toggleIt = 3
		
		await message.channel.send("Your Cards:")

		await message.channel.send(card1)
		await message.channel.send(card2)
		await message.channel.send(card3)

		if card1r == 'K':
			card11r = 10
			toggleItr = 1
		if card2r == 'K':
			card22r = 10
			toggleItr = 2
		if card3r == 'K':
			card33r = 10
			toggleItr = 4			
		if card1r == 'Q':
			card11r = 10
			toggleItr = 1
		if card2r == 'Q':
			card22r = 10
			toggleItr = 2
		if card3r == 'Q':
			card33r = 10
			toggleItr = 4	
		if card1r == 'J':
			card11r = 10
			toggleItr = 1
		if card2r == 'J':
			card22r = 10
			toggleItr = 2
		if card3r == 'J':
			card33r = 10
			toggleItr = 4	
		if card1r == 'A':
			card44r = 11
			toggleItr = 1
		if card2r == 'A':
			card55r = 11
			toggleItr = 2
		if card3r == 'A':
			card66r = 11
			toggleItr = 4



		if card1r == 'K' and card2r == 'K':
			toggleItr = 3
		if card1r == 'K' and card2r == 'Q':
			toggleItr = 3
		if card1r == 'K' and card2r == 'J':
			toggleItr = 3
		if card1r == 'Q' and card2r == 'K':
			toggleItr = 3
		if card1r == 'Q' and card2r == 'Q':
			toggleItr = 3
		if card1r == 'Q' and card2r == 'J':
			toggleItr = 3
		if card1r == 'J' and card2r == 'K':
			toggleItr = 3
		if card1r == 'J' and card2r == 'Q':
			toggleItr = 3
		if card1r == 'J' and card2r == 'J':
			toggleItr = 3
		if card1r == 'A' and card2r == 'K':
			toggleItr = 3
		if card1r == 'A' and card2r == 'Q':
			toggleItr = 3
		if card1r == 'A' and card2r == 'J':
			toggleItr = 3

		if card1r == 'K' and card3r == 'K':
			toggleItr = 3
		if card1r == 'K' and card3r == 'Q':
			toggleItr = 3
		if card1r == 'K' and card3r == 'J':
			toggleItr = 3
		if card1r == 'Q' and card3r == 'K':
			toggleItr = 3
		if card1r == 'Q' and card3r == 'Q':
			toggleItr = 3
		if card1r == 'Q' and card3r == 'J':
			toggleItr = 3
		if card1r == 'J' and card3r == 'K':
			toggleItr = 3
		if card1r == 'J' and card3r == 'Q':
			toggleItr = 3
		if card1r == 'J' and card3r == 'J':
			toggleItr = 3
		if card1r == 'A' and card3r == 'K':
			toggleItr = 3
		if card1r == 'A' and card3r == 'Q':
			toggleItr = 3
		if card1r == 'A' and card3r == 'J':
			toggleItr = 3

		if card3r == 'K' and card2r == 'K':
			toggleItr = 3
		if card3r == 'K' and card2r == 'Q':
			toggleItr = 3
		if card3r == 'K' and card2r == 'J':
			toggleItr = 3
		if card3r == 'Q' and card2r == 'K':
			toggleItr = 3
		if card3r == 'Q' and card2r == 'Q':
			toggleItr = 3
		if card3r == 'Q' and card2r == 'J':
			toggleItr = 3
		if card3r == 'J' and card2r == 'K':
			toggleItr = 3
		if card3r == 'J' and card2r == 'Q':
			toggleItr = 3
		if card3r == 'J' and card2r == 'J':
			toggleItr = 3
		if card3r == 'A' and card2r == 'K':
			toggleItr = 3
		if card3r == 'A' and card2r == 'Q':
			toggleItr = 3
		if card3r == 'A' and card2r == 'J':
			toggleItr = 3

		await message.channel.send("Dealer Cards:")

		await message.channel.send(card1r)
		await message.channel.send(card2r)
		await message.channel.send(card3r)

		if toggleIt == 1:
			if card1 == 'A' or card2 == 'A' or card3 == 'A':
				card2 = card22
				card3 = card33
				tot = 11 + card2 + card3
				if tot <= 21:
					card44 = 11
				else:
					card44 = 1

				card11 = card44

			tot = card11 + card2 + card3

		elif toggleIt == 2:
			if card1 == 'A' or card2 == 'A' or card3 == 'A':
				card1 = card11
				card3 = card33
				tot = card1 + 11 + card3
				if tot <= 21:
					card55 = 11
				else:
					card55 = 1

				card22 = card55

			tot = card1 + card22 + card3
		
		elif toggleIt == 4:
			if card1 == 'A' or card2 == 'A' or card3 == 'A':
				card1 = card11
				card2 = card22
				tot = card1 + card2 + 11		
				if tot <= 21:
					card66 = 11
				else:
					card66 = 1

				card33 = card66

			tot = card1 + card2 + card33

		elif toggleIt == 3:
			if card1 == 'A':
				card2 = card22
				card3 = card33
				tot = 11 + card2 + card3
				if tot <= 21:
					card44 = 11
					card55 = 11
					card66 = 11
				else:
					card44 = 1
					card55 = 1
					card66 = 1
				
				card11 = card44
				card22 = card55
				card33 = card66

			if card2 == 'A':
				card1 = card11
				card3 = card33
				tot = card1 + 11 + card3
				if tot <= 21:
					card44 = 11
					card55 = 11
					card66 = 11
				else:
					card44 = 1
					card55 = 1
					card66 = 1
				
				card11 = card44
				card22 = card55
				card33 = card66

			if card3 == 'A':
				card2 = card22
				card1 = card11
				tot = card1 + card2 + 11
				if tot <= 21:
					card44 = 11
					card55 = 11
					card66 = 11
				else:
					card44 = 1
					card55 = 1
					card66 = 1
				
				card11 = card44
				card22 = card55
				card33 = card66				
			
			tot = card11 + card22 + card33
		
		else:
			tot = card1 + card2 + card3
		
		if toggleItr == 1:
			if card1r == 'A' or card2r == 'A' or card3r == 'A':
				card2r = card22r
				card3r = card33r
				totr = 11 + card2r + card3r
				if totr <= 21:
					card44r = 11
				else:
					card44r = 1

				card11r = card44r

			totr = card11r + card2r + card3r

		elif toggleItr == 2:
			if card1r == 'A' or card2r == 'A' or card3r == 'A':
				card1r = card11r
				card3r = card33r
				totr = card1r + 11 + card3r
				if totr <= 21:
					card55r = 11
				else:
					card55r = 1

				card22r = card55r

			totr = card1r + card22r + card3r
		
		elif toggleItr == 4:
			if card1r == 'A' or card2r == 'A' or card3r == 'A':
				card1r = card11r
				card2r = card22r
				totr = card1r + card2r + 11		
				if totr <= 21:
					card66r = 11
				else:
					card66r = 1

				card33r = card66r

			totr = card1r + card2r + card33r

		elif toggleItr == 3:
			if card1r == 'A':
				card2r = card22r
				card3r = card33r
				totr = 11 + card2r + card3r
				if totr <= 21:
					card44r = 11
					card55r = 11
					card66r = 11
				else:
					card44r = 1
					card55r = 1
					card66r = 1
				
				card11r = card44r
				card22r = card55r
				card33r = card66r

			if card2r == 'A':
				card1r = card11r
				card3r = card33r
				totr = card1r + 11 + card3r
				if totr <= 21:
					card44r = 11
					card55r = 11
					card66r = 11
				else:
					card44r = 1
					card55r = 1
					card66r = 1
				
				card11r = card44r
				card22r = card55r
				card33r = card66r

			if card3r == 'A':
				card2r = card22r
				card1r = card11r
				totr = card1r + card2r + 11
				if totr <= 21:
					card44r = 11
					card55r = 11
					card66r = 11
				else:
					card44r = 1
					card55r = 1
					card66r = 1
				
				card11r = card44r
				card22r = card55r
				card33r = card66r			
			
			totr = card11r + card22r + card33r
		
		else:
			totr = card1r + card2r + card3r
				
		await message.channel.send("Total : {}".format(tot))
		await message.channel.send("Dealer Total : {}".format(totr))

		if tot == 21 or totr > 21 or 21 - tot > totr - 21:
			textl = "You Win! Reward : 3x Chips"
		if totr == 21 or tot > 21 or 21 - tot < totr - 21:
			textl = "You Lose! Reward : Lose Chips"
		
		await message.channel.send(textl)

	if message.content.startswith('>roulette'):
		rouletteList = [
			'10',
			'5',
			'5',
			'2',
			'2',
			'2',
			'2',
			'1',
			'1',
			'1',
			'1',
			'1',
			'0.5',
			'0.5',
			'0.5',
			'0.5',
			'0.25',
			'0.25'
		]

		rouletteChoice = random.choice(rouletteList)

		sendR = 'You recieved your chips as', rouletteChoice + 'x!'

		await message.channel.send(sendR)
	
	if message.content.startswith('>autoLottery'):

		# 10 Chips
		# Win = 830,376,562 Chips

		aNum1 = random.randint(1,45)
		aNum2 = random.randint(1,45)
		aNum3 = random.randint(1,45)
		aNum4 = random.randint(1,45)
		aNum5 = random.randint(1,45)
		aNum6 = random.randint(1,45)

		send = 'Your Numbers:', aNum1, aNum2, aNum3, aNum4, aNum5, aNum6

		await message.channel.send(send)

		if rNum1 == aNum1:
			if rNum2 == aNum2:
				if rNum3 == aNum3:
					if rNum4 == aNum4:
						if rNum5 == aNum5:
							if rNum6 == aNum6:
								await message.channel.send("You Win! (+830,376,562 Chips)")

	if message.content.startswith('>rollTen'):
		tenLuckVar = random.randint(1,10)
		tenLuckVar2 = random.randint(1,10)

		txtTenLuck = "Chosen Number :", tenLuckVar, "Rolled Number :", tenLuckVar2
		await message.channel.send(str(txtTenLuck))

		if tenLuckVar == tenLuckVar2:
			await message.channel.send("WIN! GG!")
		else:
			await message.channel.send("Try Again Next Time...")

	if message.content.startswith('>rollFifty'):
		fLuckVar = random.randint(1,50)
		fLuckVar2 = random.randint(1,50)

		txtTenLuck = "Chosen Number :", fLuckVar, "Rolled Number :", fLuckVar2
		await message.channel.send(str(txtTenLuck))

		if fLuckVar == fLuckVar2:
			await message.channel.send("WIN! GG!")
		else:
			await message.channel.send("Try Again Next Time...")

	if message.content.startswith('>rollHundred'):
		hLuckVar = random.randint(1,100)
		hLuckVar2 = random.randint(1,100)

		txtTenLuck = "Chosen Number :", hLuckVar, "Rolled Number :", hLuckVar2
		await message.channel.send(str(txtTenLuck))

		if hLuckVar == hLuckVar2:
			await message.channel.send("WIN! GG!")
		else:
			await message.channel.send("Try Again Next Time...")

client.run(os.getenv('TOKEN'))