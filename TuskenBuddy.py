'''

Author: Matthew Becker
Date: 20200224
Description: TuskenBuddy bot

'''
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from random import randint
from discord import opus


load_dotenv() # loads the .env in which the token is stored
token = os.getenv('TUSKENBUDDY_TOKEN') # gets the bot token from the .env file so that the token is not stored in main
command_prefix = '?'
bot = commands.Bot(command_prefix=commands.when_mentioned_or(command_prefix)) # sets the command prefix to be used, to the command_prefix variable

@bot.command()
async def load(ctx, extension): # loads the cogs folder
    bot.load_extension(f'cogs.{extension}')

@bot.event # Indicates when the bot is ready
async def on_ready(): # async allows discord to run multiple functions at once
    print("TuskenBuddy is running")

@bot.event # Prints deleted messages in the server, and shames the deleter
async def on_message_delete(message):
    author = message.author.mention
    content = message.content
    channel = message.channel
    await channel.send('AURGH @everyone , {} said: "{}" AUUURGH DELETED AURGH HIDING THINGS!'.format(author, content))

@bot.command() # says hello to the bot, and tells the bot to say hello back
async def hello(ctx):
    await ctx.send('AURGH AUUUURGH!')

@bot.command()
async def joinVoice(ctx): # tells the bot to join the voice channel the author is in
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command() # tells the bot to leave voice channel
async def leaveMe(ctx):
    await ctx.voice_client.disconnect()

@bot.command() # unloads the cogs folder
async def unload(ctx, extension): 
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'): # loop through cogs file
    if filename.endswith('.py'): # find each file with the .py extension
        bot.load_extension(f'cogs.{filename[:-3]}') # remove the .py from the filename

bot.run(token) # This function must be last function