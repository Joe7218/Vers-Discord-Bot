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
	if message.content.startswith('!twat'):
		zevsmsg = 'Did you mean <@!173547110388465664>'
		await client.send_message(message.channel, zevsmsg)
		
		
	


client.run('MzE4NjQ5Mzg5NjIxMTgyNDY0.DA1qUg.Lcl-HTrlzETaTBaMBJ3NsHevaAo')  
