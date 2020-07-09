from discord.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Eight Ball
    @commands.command(name='8ball', description="Answers a yes/no question.", brief="Answers from the beyond.",
    aliases=['eight_ball', 'eightball', '8-ball'], pass_context=True)
    async def eight_ball(self, ctx):
        response =[ 
            'Without a doubt.', 
            'Outlook good.', 
            'Better not tell you now.', 
            'Cannot predict now.',
            'My reply is no.', 
            'Outlook not so good.',
        ]

        await ctx.send(random.choice(response))

    # Dice Roll
    @commands.command(name='dice', description="Rolls a number 1-6", brief="Rolls those dices!", pass_context=True)
    async def dices(self, ctx):
        await ctx.send(random.randint(1,6))


def setup(bot):
    bot.add_cog(Games(bot))

