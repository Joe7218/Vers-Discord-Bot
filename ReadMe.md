# Vers-Discord-Bot
#put all of this in a main.py folder on ur comp
import discord
import asyncio

client = discord.Client()

client.event
async def on_ready():  
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_message(message):  
	# Per the discord.py docs this is to not have the bot respond to itself
	if message.author == client.user:
		return
	#If the bot sees the command !hello we will respond with our msg string
	if message.content.startswith('!hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
	if message.content.startswith('!twat'):		#the one u love
		zevsmsg = 'Did you mean <@!173547110388465664>'
		await client.send_message(message.channel, zevsmsg) "the zevsmsg has to be different form all the other msgs, it can be anything tho"
	if message.content.startswith('!shuttle'):		#shuttle
		shmsg = 'http://imgur.com/a/7NUDR'
		await client.send_message(message.channel, shmsg)
	if message.content.startswith('Vers Bot'):				#for the prefix
		bmsg = 'The prefix for this server is !'
		await client.send_message(message.channel, bmsg)
	if message.content.startswith('Vers Bot'):
		amsg = 'The prefix for this server is !'
		await client.send_message(message.channel, amsg)	
		
	


client.run('BOT TOKEN GOES HERE')
