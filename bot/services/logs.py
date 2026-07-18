import discord

from datetime import datetime

from config import TICKET_LOG_CHANNEL





async def enviar_log_ticket(

    bot,

    usuario,

    cerrado_por,

    canal,

    archivo=None

):


    log_channel = bot.get_channel(

        TICKET_LOG_CHANNEL

    )



    if log_channel is None:


        print(

            "❌ Canal de logs no encontrado"

        )

        return






    embed = discord.Embed(

        title="🛡️ RobuxGuardian | Ticket Cerrado",

        color=0xff0000

    )



    embed.add_field(

        name="🎫 Ticket",

        value=f"`{canal}`",

        inline=False

    )



    embed.add_field(

        name="👤 Usuario",

        value=str(usuario),

        inline=True

    )



    embed.add_field(

        name="🔒 Cerrado por",

        value=str(cerrado_por),

        inline=True

    )



    embed.add_field(

        name="📌 Estado",

        value="✅ Cerrado",

        inline=True

    )



    embed.add_field(

        name="📅 Fecha de cierre",

        value=datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        ),

        inline=False

    )



    embed.add_field(

        name="📄 Evidencia",

        value="✅ Generada correctamente",

        inline=True

    )



    embed.description = (

        "Sistema automático de evidencia y auditoría.\n\n"

        "RobuxGuardian Security System"

    )



    embed.set_footer(

        text="RobuxGuardian Security System"

    )







    try:



        if archivo:


            await log_channel.send(

                embed=embed,

                file=discord.File(

                    archivo

                )

            )


        else:


            await log_channel.send(

                embed=embed

            )



    except Exception as e:


        print(

            "❌ Error enviando log:",

            e

        )