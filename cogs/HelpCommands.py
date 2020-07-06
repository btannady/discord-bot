import discord
from discord.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Embedding Messages ; Help Function
    @commands.command(description="Provides list of bot commands.", pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(title="Available Commands\t\t\t\t\t\t\t")
        
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/863743347545878532/lVy3o9CT_reasonably_small.jpg")

        embed.add_field(name=":clown: Misc :clown:", value="• $hello\n• [Coming Soon]\n• [Coming Soon]\n• [Coming Soon]", inline=True)

        embed.add_field(name=":question: Help :question:", value="• $help\n• [Coming Soon]\n• [Coming Soon]\n• [Coming Soon]", inline=True)

        embed.add_field(name=":video_game: Games :video_game:", value="• $8ball\n• [Coming Soon]\n• [Coming Soon]\n• [Coming Soon]", inline=True)

        embed.add_field(name=":musical_note: Music :musical_note:", value="• [Coming Soon]\n• [Coming Soon]\n• [Coming Soon]", inline=True)

        embed.add_field(name=":performing_arts: Roleplay :performing_arts:", value="• [Coming Soon]\n• [Coming Soon]\n• [Coming Soon]", inline=True)

        # images/gifs should be 128x128 i think
        embed.set_footer(text="Bot by Wulong Tea #3823", icon_url="https://pa1.narvii.com/5921/00e44dbc58a302aaa66142c041da9a7e0ecc8a45_128.gif")

        await ctx.channel.send(content=None, embed=embed)


def setup(bot):
    bot.add_cog(HelpCommands(bot))



# Useful Links:
# Custom Embeds : https://docs.yagpdb.xyz/others/custom-embeds
# Discord Embed Generator : https://cog-creators.github.io/discord-embed-sandbox/ 
