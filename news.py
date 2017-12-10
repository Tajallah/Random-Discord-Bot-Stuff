import discord
import asyncio
from discord.ext import commands
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

def openlink (url):
	print('opening link %s'%(url))
	html = urlopen(url)
	z = riplinks(html, url)
	print(z)
	return z

def riplinks (html, url):
	q = []
	print('ripping links')
	soup = BeautifulSoup(html, 'lxml')
	for a in soup.find_all('a', href=True):
		if '/article' in a['href']:
			q.append(url+a['href'])
			print('%i found.'%(len(q)))
	print('%i found.'%(len(q)))
	return q

def doall (site):
	print('starting')
	q = openlink(site)
	return q

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-----------')
	await client.send_message(client.get_channel('CHANNEL ID AS STR'), '```News module online```')

@client.event
async def on_message(message):
	if (message.content.startswith('!headlines ')):
		x = int(message.content.replace('!headlines ', ''))
		links = doall("https://www.reuters.com")
		await client.send_message(message.channel, 'Here are some headlines for you.')
		print(links)
		print('Printing headlines')
		for n in range(1, x+1):
			await client.send_message(message.channel, '%s'%(links[n]))
	
	elif (message.content == 'END NEWS MODULE'):
		await client.send_message(message.channel, 'News module shutting down')
		client.close()
		raise SystemExit

client.run('BOT TOKEN GOES HERE')
