import discord

from db.database import conectar

from datetime import datetime

from utils.embeds import (
    embed_analisis,
    embed_verificacion
)

from views.ticket_buttons import TicketButtons





class TicketManager:


    @staticmethod
    async def crear_ticket(interaction: discord.Interaction):


        guild = interaction.guild


        if guild is None:

            return None



        categoria = discord.utils.get(

            guild.categories,

            name="🎫 TICKETS"

        )



        if categoria is None:


            categoria = await guild.create_category(

                "🎫 TICKETS"

            )





        permisos = {


            guild.default_role:

            discord.PermissionOverwrite(

                view_channel=False

            ),



            interaction.user:

            discord.PermissionOverwrite(

                view_channel=True,

                send_messages=True,

                read_message_history=True

            ),



            guild.me:

            discord.PermissionOverwrite(

                view_channel=True,

                send_messages=True,

                manage_channels=True,

                embed_links=True

            )

        }





        canal = await guild.create_text_channel(

            name=f"ticket-{interaction.user.name}",

            category=categoria,

            overwrites=permisos

        )





        db = conectar()

        cursor = db.cursor()



        cursor.execute(

            """

            INSERT INTO tickets

            (

            user,

            subject,

            message,

            status,

            created_at

            )

            VALUES(?,?,?,?,?)

            """,

            (

                str(interaction.user.id),

                "Ticket Discord",

                canal.name,

                "Pendiente",

                datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"

                )

            )

        )


        db.commit()

        db.close()





        # ANALISIS

        try:


            await canal.send(

                embed=embed_analisis(

                    interaction.user

                )

            )


        except Exception as e:


            print(

                "❌ Error análisis:",

                e

            )







        # VERIFICACION


        await canal.send(

            embed=embed_verificacion(

                interaction.user

            ),

            view=TicketButtons(

                interaction.client

            )

        )



        return canal