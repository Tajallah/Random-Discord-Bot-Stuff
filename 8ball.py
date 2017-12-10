import random
import sys
import discord
import asyncio
from discord.ext import commands

client = discord.Client()

outcomes = [ 'It is certain', 'It is decidedly so.', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful', 'Don\'t ever talk to me or my 20 sided dice ever again', ':^)']


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-----------')
	await client.send_message(client.get_channel('CHANNEL ID AS STR'), 'News module online')

@client.event
async def on_message(message):
	if message.content.startswith('!8ball'):
		ra = random.randint(0, 21)
		await client.send_message(message.channel, ':8ball: %s'%(outcomes[ra]))

client.run('BOT TOKEN GOES HERE')
