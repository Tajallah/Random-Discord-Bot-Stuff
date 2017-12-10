import datetime
import sys
import discord
import asyncio
import json
import os
client = discord.Client()
owner_id = #must be a str

@client.event
#This executes when the bot connects to the channel
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-----------')
	await client.send_message(client.get_channel('REPLACE THIS WITH THE CHANNEL ID'), '```(testing)```')

@client.event
#All of these are responses to user messages
async def on_message(message):
	#makes this stuff easier to type out
	message.content = mc
	#Collects logs in order to train on them later.
	if(message.author != client.user and not mc.startswith('!')):
		print("Writing \"%s\" to the dataset"%(message.content))
		if (os.path.isfile('trainingset') == False):
			print("NO TRANSCRIPT FOUND. MAKING A NEW ONE")
		transcript = open('trainingset', 'a+')
		transcript.write(mc)
		transcript.write("\n")
		transcript.close()
	else:
		print("skiping self message")	
	
	#Kills this module. Only works if the owner says it.
	elif mc.startswith('!sleep'):
		if (message.author.id == owner_id):
			await client.send_message(message.channel, '```K. I\'m dead now. Looks like Anon is going to do maintainence on me or something.```')
			client.close()
			raise SystemExit
		else:
			await client.send_message(message.channel, 'I don\'t answer to you m8.')
	#replies with a random fortune out of the pre-created fortune pool
	elif mc.startswith('!fortune'):
		now = datetime.datetime.now()
		fortunes = ['Your fortune: Reply hazy, try again', 'Your fortune: Excellent Luck', 'Your fortune: Good Luck', 'Your fortune: Average Luck', 'Your fortune: Bad Luck','Your fortune: Good news will come to you by mail', 'Your fortune: （　´_ゝ`）ﾌｰﾝ', 'Your fortune: ｷﾀ━━━━━━(ﾟ∀ﾟ)━━━━━━ !!!!', 'Your fortune: You will meet a dark handsome stranger', 'Your fortune: Better not tell you now', 'Your fortune: Outlook good', 'Your fortune: Very Bad Luck', 'Your fortune: Godly Luck']
		pick = now.microsecond%13
		await client.send_message(message.channel, fortunes[pick])

	#posts a pre-designated meme TODO: Seperate this into a different meme module and expand functionality
	elif mc.startswith('!meme'):
		await client.send_file(message.channel, 'memes/meme.png')
	
	#posts an ancap smiley TODO: Seperate this one too.
	elif mc.startswith('!ancap'):
                await client.send_file(message.channel, 'ancappy.png')

	#Ayy >> LMAO
	elif (mc == 'ayy' or mc == 'Ayy' or mc == 'AYY'):
		await client.send_message(message.channel, 'lmao')
	
client.run('REPLACE THIS WITH THE BOT TOKEN')
