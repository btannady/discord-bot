from discord.ext import commands
from riotwatcher import LolWatcher, ApiError
import pandas as pd

import requests

class League(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    # User says $hello we will send back hi
    @commands.command(name='league', description="Give Live Game League of Legends stats.", brief="LoL Live Game Stats!")
    async def league(self, ctx):
        
        # golbal variables
        api_key = 'RGAPI-09bfc3de-6501-486c-a41a-0989a1fb7b94'
        watcher = LolWatcher(api_key)
        my_region = 'na1'

        if len(ctx.message.content[9:]) > 0:
            userPhrase = ctx.message.content[9:]
            # Basic Account Info
            me = watcher.summoner.by_name(my_region, userPhrase)
            # Get info on Live Game Statistics
            currentGameInfo = 'https://' + my_region + '.api.riotgames.com' + '/lol/spectator/v4/active-games/by-summoner/' + me['id'] + '?api_key=' + api_key
            response = requests.get(currentGameInfo)
            
            # Check if player is in a Live Game right now.
            if (str(response) == '<Response [404]>'):
                
                await ctx.channel.send("The summoner isn't in-game right now, please try retry later. The game needs be on the loading screen or it must have started.")
                
            else:
                
                # Prepare dictionary for Live Game info of each player
                #currentSummmoner = {'summonerName':'', 'currentSoloRank':'', 'previousSoloRank':'', 'champion':''}

                print('\nSummoners in Current Live Game:')
                for participant in response.json()['participants']:
                    
                    # ---------------------------------------
                    await ctx.channel.send("Summoner Name: " + participant['summonerName'])
                    # ---------------------------------------
                    await ctx.channel.send("Champion ID: " + str(participant['championId']))
                    # ---------------------------------------
                    await ctx.channel.send("Summoner ID: " + participant['summonerId'])


                    currSumID = participant['summonerId']
                    
                    # ---------------------------------------
                    # Access Rank Informationn

                    # Return the rank status for a player
                    my_ranked_stats = watcher.league.by_summoner(my_region, currSumID)


                    # display for MY personal use for easier read
                    for rankedType in my_ranked_stats:
                        await ctx.channel.send(rankedType['tier'] + " " + rankedType['rank'])
                    # ---------------------------------------

                    await ctx.channel.send("---------------------------------------")
 
            #await ctx.channel.send(userPhrase)
        else:
            await ctx.channel.send("You didn't give me a League username to search! :c")


def setup(bot):
    bot.add_cog(League(bot))