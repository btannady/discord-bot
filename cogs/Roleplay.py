from discord.ext import commands
import discord
import random

class Roleplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Send explosion gif
    @commands.command(name='explosion', description="Send explosion gif!", brief="EXPLOSION!!", pass_context=True)
    async def explo(self, ctx):
        gifList =[
            'https://media1.tenor.com/images/7b898ab00319df6fbe918f1e6e860a16/tenor.gif?itemid=16739385', 
            'https://media1.tenor.com/images/5fc8e2cde6b8adcbed9419885f72239e/tenor.gif?itemid=13300624',
            'https://media1.tenor.com/images/5da736bd133f8900240b03775277477c/tenor.gif?itemid=17442817',
            'https://media1.tenor.com/images/479c8d90003475763785baeb0bb2ad38/tenor.gif?itemid=14523572',
            'https://media1.tenor.com/images/b7f6ca5543682994e1ff2ffe4db42d06/tenor.gif?itemid=14523550',
            'https://media1.tenor.com/images/a5200ff8939402e4e2bbda3a8107d2b1/tenor.gif?itemid=7559840'

        ]

        embed = discord.Embed(title="EXPLOSION!!!!\t\t\t\t\t\t\t")
        embed.set_image(url=random.choice(gifList))
        await ctx.channel.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(Roleplay(bot))