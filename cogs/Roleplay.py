from discord.ext import commands
import discord
import random

class Roleplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Remember case to check user input --> function name size + commandPrefix size + 1 = x in ctx.message.content[x:]
    # ********************************************************************************************************

    # Send explosion gif
    @commands.command(name='explosion', description="Send explosion gif!", brief="EXPLOSION!!", pass_context=True)
    async def explosion(self, ctx):
        gifList =[
            'https://media1.tenor.com/images/7b898ab00319df6fbe918f1e6e860a16/tenor.gif?itemid=16739385', 
            'https://media1.tenor.com/images/5fc8e2cde6b8adcbed9419885f72239e/tenor.gif?itemid=13300624',
            'https://media1.tenor.com/images/5da736bd133f8900240b03775277477c/tenor.gif?itemid=17442817',
            'https://media1.tenor.com/images/479c8d90003475763785baeb0bb2ad38/tenor.gif?itemid=14523572',
            'https://media1.tenor.com/images/b7f6ca5543682994e1ff2ffe4db42d06/tenor.gif?itemid=14523550',
            'https://media1.tenor.com/images/a5200ff8939402e4e2bbda3a8107d2b1/tenor.gif?itemid=7559840',
            'https://media1.tenor.com/images/0dcb39a6072712d02493aa368f0d522d/tenor.gif?itemid=14987251',
            'https://media1.tenor.com/images/9dba88f3aa2f93a5848aac8dc4860e0c/tenor.gif?itemid=17239287'

        ]
        if len(ctx.message.content[12:]) > 0:
            userPhrase = ctx.message.content[12:]
            embed = discord.Embed(name="EXPLOSION Gif", description= ctx.message.author.name + " uses EXPLOSION Magic" + userPhrase)
            embed.set_image(url=random.choice(gifList))
            await ctx.channel.send(content=None, embed=embed)
        else:
            embed = discord.Embed(name="EXPLOSION Gif", description= ctx.message.author.name + " uses EXPLOSION!!!!")
            embed.set_image(url=random.choice(gifList))
            await ctx.channel.send(content=None, embed=embed)

    # ********************************************************************************************************

    # Send cry gif
    @commands.command(name='cry', description="Send cry gif!", brief="WAHHHH!!", aliases=['sad'], pass_context=True)
    async def cry(self, ctx):
        gifList =[
            'https://media1.tenor.com/images/b0f4b5f158e8a964adbabd048fb9e556/tenor.gif?itemid=13949015',
            'https://media1.tenor.com/images/75edc9882e5175f86c2af777ffbb14a6/tenor.gif?itemid=5755232',
            'https://media1.tenor.com/images/98466bf4ae57b70548f19863ca7ea2b4/tenor.gif?itemid=14682297',
            'https://media1.tenor.com/images/4f22255d60f3f19edf9296992b4e3483/tenor.gif?itemid=4772697',
            'https://media1.tenor.com/images/7618310e4332bd3303acb414348e475c/tenor.gif?itemid=5755226',
            'https://media1.tenor.com/images/74136d207293d1b32e89c1bd9338ddb2/tenor.gif?itemid=16934082',
            'https://media1.tenor.com/images/554e37d6c8e802242371ad7a7d7797cd/tenor.gif?itemid=10483341',
            'https://media1.tenor.com/images/8e1154f1bfe2f620209dc18e886aaf76/tenor.gif?itemid=16557202',
            'https://media1.tenor.com/images/08292e5af7bfddff5a55e3447ccbb9c2/tenor.gif?itemid=10483373',
            'https://media1.tenor.com/images/54d4a336509c43ec467ff3af5794ffb7/tenor.gif?itemid=12065796',
            'https://media1.tenor.com/images/0b1441502ddc1dacfc74ccf82eb32d2d/tenor.gif?itemid=12497551',
            'https://media1.tenor.com/images/8d4dd59c053f9a8af24795ffb9507120/tenor.gif?itemid=13988059',
            'https://media1.tenor.com/images/b5bb83af86ea8f2d2f5ef94ebd742edf/tenor.gif?itemid=15570527'

        ]
        if len(ctx.message.content[6:]) > 0:
            userPhrase = ctx.message.content[6:]
            embed = discord.Embed(name="Cry Gif", description= ctx.message.author.name + " cries " + userPhrase)
            embed.set_image(url=random.choice(gifList))
            await ctx.channel.send(content=None, embed=embed)
        else:
            embed = discord.Embed(name="Cry Gif", description= ctx.message.author.name + " cries")
            embed.set_image(url=random.choice(gifList))
            await ctx.channel.send(content=None, embed=embed)

    # ********************************************************************************************************

    # Send angry gif
    @commands.command(name='angry', description="Send angry gif!", brief="GRRRAAHHHHHHH!!", pass_context=True)
    async def angry(self, ctx):
        gifList =[
            'https://media1.tenor.com/images/2f198dc24f638fc9f16776c8ebd183fd/tenor.gif?itemid=14682313',
            'https://media1.tenor.com/images/ef0ede60c9425f03f3540b8d34d61535/tenor.gif?itemid=7302937',
            'https://media1.tenor.com/images/199728c74eb00a12d2d2c8a1ad440574/tenor.gif?itemid=14666121',
            'https://media1.tenor.com/images/e01bb53f5def3cd0774bfc51cd655c1d/tenor.gif?itemid=9181465',
            'https://media1.tenor.com/images/f36c46ab3916812bdd52528ccc747d7e/tenor.gif?itemid=13451230',
            'https://media1.tenor.com/images/59a525f14268587c26620522b1b02eea/tenor.gif?itemid=17747074',
            'https://media1.tenor.com/images/be01e865ad1b015090604643dcabee91/tenor.gif?itemid=5235529',
            'https://media1.tenor.com/images/60c47b399f3d058b9ad375337e04ffa8/tenor.gif?itemid=14403579'

        ]
        if len(ctx.message.content[8:]) > 0:
            userPhrase = ctx.message.content[8:]
            embed = discord.Embed(name="Angry Gif", description= ctx.message.author.name + " is furious " + userPhrase)
            embed.set_image(url=random.choice(gifList))
            await ctx.channel.send(content=None, embed=embed)
        else:
            embed = discord.Embed(name="Angry Gif", description= ctx.message.author.name + " is furious")
            embed.set_image(url=random.choice(gifList))
            await ctx.channel.send(content=None, embed=embed)

    # ********************************************************************************************************

    # Send punch gif
    @commands.command(name='punch', description="Send punch gif!", brief="SMASSHHUUUUU!!", aliases=['smash'], pass_context=True)
    async def punch(self, ctx):
        gifList =[
            'https://media1.tenor.com/images/b2db2a7fe0b9f68f2869b4e0d11a9490/tenor.gif?itemid=8932977',
            'https://media1.tenor.com/images/908f81484e9e67f0bff6593417ee009c/tenor.gif?itemid=16820809',
            'https://media1.tenor.com/images/7bdfaef4f77a6849c1213fb0ba13f183/tenor.gif?itemid=5208049',
            'https://media1.tenor.com/images/bfbddce813ae876243f4189041b64e26/tenor.gif?itemid=15004790',
            'https://media1.tenor.com/images/f0a500c18080f41afcd504ae2d1a32a6/tenor.gif?itemid=17517118',
            'https://media1.tenor.com/images/855c900190fb6abfabaed7da4da6f73c/tenor.gif?itemid=16962926',
            'https://media1.tenor.com/images/31003b964b358e937ec43ebeb7774d4c/tenor.gif?itemid=14137100',
            'https://media1.tenor.com/images/40855e799a1409c9e7d1cc804db71c19/tenor.gif?itemid=17339613',
            'https://media1.tenor.com/images/ee7e52abbf2f0bf3d4238d026bbb20df/tenor.gif?itemid=17315013',
            'https://media1.tenor.com/images/ce1db104460b97df6d4691e144ca33b0/tenor.gif?itemid=17019613',
            'https://media1.tenor.com/images/f9794270d7fa59618ef8b5c5715db137/ten`or.gif?itemid=17237749',
            'https://media1.tenor.com/images/098940a0a9e7f6c04cf5df5929a47d53/tenor.gif?itemid=10068397',
            'https://media1.tenor.com/images/fce9000e87cf5e1c77332b97261d8c40/tenor.gif?itemid=5116283',
            'https://media1.tenor.com/images/c3a7bd331727a45ebc5a5ca34ffa2b97/tenor.gif?itemid=16196310',
            'https://media1.tenor.com/images/3c95ca85f89068660becde7a31f0f04d/tenor.gif?itemid=4973550',
            'https://media1.tenor.com/images/ccbed01a816d7497c0455b5ac57a04ec/tenor.gif?itemid=3554073',
            'https://media1.tenor.com/images/5511a8309a1719987a27aa7b1ee7da04/tenor.gif?itemid=12303482'

        ]
        if len(ctx.message.content[8:]) > 0:
            userPhrase = ctx.message.content[8:]
            embed = discord.Embed(name="Punch Gif", description= ctx.message.author.name + " punches " + userPhrase)
            embed.set_image(url=random.choice(gifList))
            await ctx.channel.send(content=None, embed=embed)
        else:
            embed = discord.Embed(name="Punch Gif", description= ctx.message.author.name + " punches")
            embed.set_image(url=random.choice(gifList))
            await ctx.channel.send(content=None, embed=embed)


def setup(bot):
    bot.add_cog(Roleplay(bot))