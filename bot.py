import discord
from discord.ext import commands #enables prefix
import time
import asyncio
import random
import urllib.parse, urllib.request, re

#client = discord.Client(command_prefix='$')
bot = commands.Bot(command_prefix='$') # define the command decorator

# requires so that we can use our OWN $help command
bot.remove_command('help')

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
    bad_words = "motherfucker", "asshole", "faggot", "cunt", "bitch", "nigga", "slut", "twat", "nigger", "dyke"

    for word in bad_words:
        if message.content.lower().count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)
            await message.channel.send("Don't be toxic you baka!! Hmphh!! >:'C")

    # ****************************************** 

    # bypasses bot so it will check for commands
    await bot.process_commands(message)

# ********************************************************************************************************
#@commands.command(pass_context=True)
#async def hug(self, ctx):
   # await self.bot.say("hugs {}".format(ctx.message.author.mention()))

# ********************************************************************************************************

extensions = ['cogs.Games', 'cogs.Misc', 'cogs.HelpCommands']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)

bot.run('NzI3MjkyOTYxMzgwODkyNzkz.Xv6orQ.Bq7J8kMx_tcxHZzexqbONARnuY0')