from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # User says $hello we will send back hi
    @commands.command(name='hello', description="Welcome the user.", brief="Share a warm welcoming!")
    async def hello(self, ctx):
        await ctx.channel.send("Hello Kazuma-kun!")


def setup(bot):
    bot.add_cog(Misc(bot))