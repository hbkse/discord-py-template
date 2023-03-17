import discord
from discord.ext import commands
import logging
import requests

log = logging.getLogger(__name__)

class Misc(commands.Cog):
    """Miscellaneous commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send('pong')

    @commands.command()
    async def echo(self, ctx: commands.Context, content: str):
        await ctx.send(content)

    @commands.command()
    async def debug(self, ctx: commands.Context):
        message = [
            f'Logged in as: {self.bot.user}',
            f'Discord.py version: {discord.__version__}',
            f'Visible guilds: {self.bot.guilds}',
            f'Owner Id: {self.bot.owner_id}'
        ]
        log.info("Debug command used.")

        await ctx.send("\n".join(message))
    
    @commands.command()
    @commands.is_owner()
    async def set_profile_pic(self, ctx: commands.Context, url: str):
        response = requests.get(url)
        data = response.content
        await self.bot.user.edit(avatar=data)


async def setup(bot):
    await bot.add_cog(Misc(bot))