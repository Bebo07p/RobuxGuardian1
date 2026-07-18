import discord

from discord.ext import commands

from discord import app_commands

from services.ticket_manager import TicketManager





class Tickets(commands.Cog):


    def __init__(self, bot):

        self.bot = bot





    @app_commands.command(

        name="ticket",

        description="Crear un ticket de soporte"

    )

    async def ticket(

        self,

        interaction: discord.Interaction

    ):


        await interaction.response.defer(

            ephemeral=True

        )



        canal = await TicketManager.crear_ticket(

            interaction

        )



        await interaction.followup.send(

            f"✅ Ticket creado correctamente: {canal.mention}",

            ephemeral=True

        )







async def setup(bot):


    await bot.add_cog(

        Tickets(bot)

    )


    print(

        "✅ Tickets cargado"

    )