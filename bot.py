import discord
from discord.ext import commands #enables prefix
import time
import asyncio
import random
import os
import urllib.parse, urllib.request, re

bot = commands.Bot(command_prefix='m!') # define the command decorator

# requires so that we can use our OWN $help command
bot.remove_command('help')

# ********************************************************************************************************
# Bot comes online
@bot.event
async def on_ready():

    # updates the bot's status
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('m!help'))

    # bot greets everyone when joining the call
    
    # load music.py
    bot.load_extension('cogs.music')


# ********************************************************************************************************

# Welcome Users to Channel
@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "thetavern": # we check to make sure we're sending messages in specific channel
            await channel.send_message(f"""Welcome to the server {member.mention}""")
    
# ********************************************************************************************************

@bot.event
async def on_message(message):

    # ignores messages that the bot says
    if message.author == bot.user:
        return

    # ******************************************

    # deletes naughty words from chat
    bad_words = "nerd", "ugly"

    for word in bad_words:
        if message.content.lower().count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)
            await message.channel.send("You said a bad word!! >:'C")

    # ****************************************** 

    # bypasses bot so it will check for commands
    await bot.process_commands(message)

# ********************************************************************************************************
#@commands.command(pass_context=True)
#async def hug(self, ctx):
   # await self.bot.say("hugs {}".format(ctx.message.author.mention()))

# ********************************************************************************************************

extensions = ['cogs.Games', 'cogs.Misc', 'cogs.HelpCommands', 'cogs.Roleplay', 'cogs.League']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

bot.run('NzI3MjkyOTYxMzgwODkyNzkz.XweTfA.rsVqHJ3fxs33DsutxzWEMgY779Y')
