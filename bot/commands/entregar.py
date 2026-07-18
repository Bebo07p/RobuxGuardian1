import discord

from discord.ext import commands

from discord import app_commands

from db.database import conectar

from services.analysis import UserAnalysis

from datetime import datetime





class Entregar(commands.Cog):


    def __init__(self, bot):

        self.bot = bot







    @app_commands.command(

        name="entregar",

        description="Registrar entrega de Robux a un usuario"

    )

    @app_commands.describe(

        usuario="Usuario de Discord que recibió Robux",

        cantidad="Cantidad de Robux entregados",

        motivo="Motivo de la entrega"

    )

    async def entregar(

        self,

        interaction: discord.Interaction,

        usuario: discord.Member,

        cantidad: int,

        motivo: str

    ):



        await interaction.response.defer()





        try:



            db = conectar()

            cursor = db.cursor()



            fecha = datetime.now().strftime(

                "%Y-%m-%d %H:%M:%S"

            )





            # Guardar entrega

            cursor.execute(

                """

                INSERT INTO deliveries

                (

                discord_id,

                discord_username,

                amount,

                reason,

                delivered_by,

                created_at

                )

                VALUES(?,?,?,?,?,?)

                """,

                (

                    str(usuario.id),

                    str(usuario),

                    cantidad,

                    motivo,

                    str(interaction.user),

                    fecha

                )

            )





            db.commit()

            db.close()






            # Actualizar análisis

            UserAnalysis.actualizar_entrega(

                str(usuario.id),

                cantidad

            )







            # Obtener datos

            datos = UserAnalysis.obtener(

                str(usuario.id)

            )





            total_entregas = datos[3]

            total_robux = datos[4]







            embed = discord.Embed(

                title="💎 RobuxGuardian | Entrega Registrada",

                color=0x00ff99

            )



            embed.add_field(

                name="👤 Usuario",

                value=usuario.mention,

                inline=False

            )


            embed.add_field(

                name="💎 Cantidad",

                value=f"{cantidad} Robux",

                inline=True

            )


            embed.add_field(

                name="📦 Total entregado",

                value=f"{total_robux} Robux",

                inline=True

            )


            embed.add_field(

                name="🎟️ Entregas realizadas",

                value=str(total_entregas),

                inline=True

            )


            embed.add_field(

                name="📝 Motivo",

                value=motivo,

                inline=False

            )


            embed.add_field(

                name="🛡️ Entregado por",

                value=interaction.user.mention,

                inline=False

            )


            embed.set_footer(

                text="RobuxGuardian Security System"

            )





            await interaction.followup.send(

                embed=embed

            )






        except Exception as e:


            print(

                "❌ Error entrega Robux:",

                e

            )


            await interaction.followup.send(

                "❌ Ocurrió un error registrando la entrega."

            )









async def setup(bot):


    await bot.add_cog(

        Entregar(bot)

    )


    print(

        "✅ Entregar cargado"

    )