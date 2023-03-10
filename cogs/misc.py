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
    @commands.is_owner()
    async def debug(self, ctx):
        message = [
            f'Logged in as: {self.bot.user}',
            f'Discord.py version: {discord.__version__}',
            f'Visible guilds: {self.bot.guilds}'
        ]
        self.logger.info("Debug command used.")

        await ctx.send("\n".join(message))
    
    @commands.command()
    @commands.is_owner()
    async def set_profile_pic(self, ctx, url):
        try:
            async with self.bot.session.get(url) as resp:
                data = await resp.read()
                await self.bot.user.edit(avatar=data)
            await ctx.send("Profile picture updated!")
        except Exception as e:
            await ctx.send(f"Error: {e}")


async def setup(bot):
    await bot.add_cog(Misc(bot))