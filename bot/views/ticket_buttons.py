import discord

from datetime import datetime

from db.database import conectar

from services.evidence import generar_evidencia
from services.logs import enviar_log_ticket





class TicketButtons(discord.ui.View):


    def __init__(self, bot):

        self.bot = bot

        super().__init__(

            timeout=None

        )







    @discord.ui.button(

        label="🔒 Cerrar Ticket",

        style=discord.ButtonStyle.danger,

        custom_id="close_ticket"

    )

    async def cerrar(

        self,

        interaction: discord.Interaction,

        button: discord.ui.Button

    ):


        canal = interaction.channel



        if canal is None:


            await interaction.response.send_message(

                "❌ No se pudo encontrar el canal.",

                ephemeral=True

            )

            return






        await interaction.response.send_message(

            "🔒 Generando evidencia y cerrando ticket...",

            ephemeral=True

        )







        archivo = None




        try:


            # ==========================
            # GENERAR EVIDENCIA HTML
            # ==========================


            archivo = generar_evidencia(

                canal.name,

                str(interaction.user)

            )



            if archivo:


                await canal.send(

                    "📄 Evidencia generada correctamente."

                )


            else:


                await canal.send(

                    "⚠️ No se encontraron mensajes para guardar."

                )




        except Exception as e:


            print(

                "❌ Error generando evidencia:",

                e

            )



            await canal.send(

                "❌ Error creando evidencia."

            )








        # ==========================
        # ACTUALIZAR SQLITE
        # ==========================

        try:

            db = conectar()

            cursor = db.cursor()

            cursor.execute(

                """

                UPDATE tickets

                SET

                    status = ?,

                    closed_by = ?,

                    closed_at = ?

                WHERE message = ?

                """,

                (

                    "Cerrado",

                    str(interaction.user),

                    datetime.now().strftime(

                        "%Y-%m-%d %H:%M:%S"

                    ),

                    canal.name

                )

            )

            db.commit()

            db.close()

            print(

                f"✅ Ticket actualizado: {canal.name}"

            )

        except Exception as e:

            print(

                "❌ Error actualizando ticket:",

                e

            )








        # ==========================
        # ENVIAR LOG
        # ==========================


        try:


            await enviar_log_ticket(

                self.bot,

                canal.guild.get_member(

                    interaction.user.id

                ),

                interaction.user,

                canal.name,

                archivo

            )


        except Exception as e:


            print(

                "❌ Error enviando log:",

                e

            )








        # ==========================
        # ELIMINAR CANAL
        # ==========================


        await canal.delete()










    @discord.ui.button(

        label="👤 Reclamar Ticket",

        style=discord.ButtonStyle.primary,

        custom_id="claim_ticket"

    )

    async def reclamar(

        self,

        interaction: discord.Interaction,

        button: discord.ui.Button

    ):


        from db.database import conectar

        from datetime import datetime



        canal = interaction.channel



        if canal is None:

            return






        db = conectar()

        cursor = db.cursor()





        # Revisar si ya fue reclamado

        cursor.execute(

            """

            SELECT claimed_by

            FROM tickets

            WHERE message = ?

            """,

            (

                canal.name,

            )

        )



        resultado = cursor.fetchone()





        if resultado and resultado[0]:


            db.close()


            await interaction.response.send_message(

                "⚠️ Este ticket ya fue reclamado.",

                ephemeral=True

            )

            return






        # Guardar reclamación

        cursor.execute(

            """

            UPDATE tickets

            SET

            claimed_by = ?,

            claimed_at = ?,

            status = ?

            WHERE message = ?

            """,

            (

                str(interaction.user),

                datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"

                ),

                "En revisión",

                canal.name

            )

        )



        db.commit()

        db.close()







        embed = discord.Embed(

            title="👤 Ticket reclamado",

            color=0x3498DB

        )



        embed.add_field(

            name="🛡️ Staff asignado",

            value=interaction.user.mention,

            inline=False

        )



        embed.add_field(

            name="📌 Estado",

            value="En revisión",

            inline=True

        )



        embed.add_field(

            name="📅 Fecha",

            value=datetime.now().strftime(

                "%Y-%m-%d %H:%M:%S"

            ),

            inline=True

        )



        embed.set_footer(

            text="RobuxGuardian Security System"

        )





        await interaction.response.send_message(

            embed=embed

        )