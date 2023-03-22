import discord
from discord import app_commands
from discord.ext import commands
import logging

log: logging.Logger = logging.getLogger(__name__)

class Example(commands.Cog):
    """Example commands so I can remember how these work"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx: commands.Context):
        """Basic message command"""
        await ctx.send('pong')

    # embed and button example
    # For a better example: 
    # https://github.com/Rapptz/discord.py/blob/064cbd11254e0862e4637093b969cf6cdb020608/examples/views/counter.py
    @app_commands.command(name="button-example")
    async def button_example(self, interaction: discord.Interaction) -> None:
        """ /button-example """
        embed = discord.Embed(title='Button Example')

        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
        embed.timestamp = interaction.created_at
        embed.description = "Button Counter Example"

        # Define a simple View that gives us a counter button
        class Counter(discord.ui.View):

            # Define the actual button
            # When pressed, this increments the number displayed until it hits 5.
            # When it hits 5, the counter button is disabled and it turns green.
            # note: The name of the function does not matter to the library
            @discord.ui.button(label='0', style=discord.ButtonStyle.red)
            async def count(self, interaction: discord.Interaction, button: discord.ui.Button):
                number = int(button.label) if button.label else 0
                if number + 1 >= 5:
                    button.style = discord.ButtonStyle.green
                    button.disabled = True
                button.label = str(number + 1)

                # Make sure to update the message with our updated selves
                await interaction.response.edit_message(view=self)

        await interaction.channel.send(embed=embed, view=Counter())

    # https://gist.github.com/AbstractUmbra/a9c188797ae194e592efe05fa129c57f
    @app_commands.command(name="echo-example")
    @app_commands.describe(message="string that will be sent")
    async def echo_example(self, interaction: discord.Interaction, message: str) -> None:
        """ /echo-example {message} """
        await interaction.response.send_message(message, ephemeral=True)

    # Context menu example
    # https://github.com/Rapptz/discord.py/blob/064cbd11254e0862e4637093b969cf6cdb020608/examples/app_commands/basic.py#L94
    @app_commands.context_menu(name='Report Message Example')
    async def report_message(interaction: discord.Interaction, message: discord.Message):
        # We're sending this response message with ephemeral=True, so only the command executor can see it
        await interaction.response.send_message(
            f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
        )

        # Should send to an admin reporting channel, but here we just send it back
        log_channel = interaction.channel  

        embed = discord.Embed(title='Reported Message')
        if message.content:
            embed.description = message.content

        embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
        embed.timestamp = message.created_at

        url_view = discord.ui.View()
        url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

        await log_channel.send(embed=embed, view=url_view)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Example(bot))