import discord
from discord.ext import commands
import logging

log = logging.getLogger(__name__)

class Misc(commands.Cog):
    """Miscellaneous commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send('pong')

    @commands.command()
    @commands.is_owner()
    async def debug(self, ctx: commands.Context):
        message = [
            f'Logged in as: {self.bot.user}',
            f'Discord.py version: {discord.__version__}'
        ]
        log.info("Debug command used.")

        await ctx.send("\n".join(message))

    # TODO: load_cog, unload_cog, server_list, python eval(?), tail recent logs


async def setup(bot):
    await bot.add_cog(Misc(bot))