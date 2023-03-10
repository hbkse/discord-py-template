import discord
from discord.ext import commands
import logging
import config


class Misc(commands.Cog):
    """Miscellaneous commands."""

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('zhenpai.misc')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command()
    async def echo(self, ctx, content):
        await ctx.send(content)

    @commands.command()
    async def debug(self, ctx):
        message = [
            f'Logged in as: {self.bot.user}',
            f'Discord.py version: {discord.__version__}',
            f'Visible guilds: {self.bot.guilds}'
        ]

        await ctx.send("\n".join(message))

async def setup(bot):
    await bot.add_cog(Misc(bot))