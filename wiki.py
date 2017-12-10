import re
import wikipedia
import sys
import discord
import asyncio
import json
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-----------')
	#await client.send_message(client.get_channel('CHANNEL ID AS STR'), 'News module online')

@client.event
async def on_message(message):
	if message.content.startswith('!wiki '):
		if ('?' in message.content):
			queery = message.content[6:]
			queery = queery.replace('?', '')
			ls = wikipedia.search(queery)
			q = ''
			for i in ls:
				q += '**' + i + '**\n'
			await client.send_message(message.channel, 'For the term %s I found these possible Wikipedia pages.'%(queery))
			await (client.send_message(message.channel, q))

		else:
			queery = message.content[6:]
			try:
				summary = wikipedia.summary(queery)
				await client.send_message(message.channel, '**%s: ** %s'%(queery, summary))
				full = wikipedia.page(queery)
				await client.send_message(message.channel, full.url)
			except wikipedia.exceptions.DisambiguationError as e:
				options = e.options
				await (client.send_message(message.channel, 'Hmm, some clarification is needed? What did you mean by this?'))
				q = ''
				for i in options:
					 q += '**' + i + '**\n'
				await (client.send_message(message.channel, q))

client.run('BOT TOKEN GOES HERE')
