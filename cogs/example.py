import discord
from discord.ext import commands
import logging

log: logging.Logger = logging.getLogger(__name__)

class Example(commands.Cog):
    """Example commands so I can remember how these work"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def ping(self, ctx: commands.Context):
        await ctx.send('pong')

    # button example

    # slash command example

async def setup(bot):
    await bot.add_cog(Example(bot))