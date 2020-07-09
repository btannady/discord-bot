from discord.ext import commands

class Roleplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Send explosion gif
    @commands.command(name='explosion', description="Send explosion gif!", brief="EXPLOSION!!", pass_context=True)
    async def explo(self, ctx):
        #await ctx.channel.send(file=discord.File('gifs/explosionPic1.jpg'))
        await ctx.send("gifs/explosionPic1.jpg")

def setup(bot):
    bot.add_cog(Roleplay(bot))