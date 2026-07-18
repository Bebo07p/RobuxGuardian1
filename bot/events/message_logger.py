import discord

from discord.ext import commands

from datetime import datetime

from db.database import conectar





class MessageLogger(commands.Cog):


    def __init__(self, bot):

        self.bot = bot







    @commands.Cog.listener()

    async def on_message(

        self,

        message: discord.Message

    ):


        print(

            "📩 MENSAJE:",

            message.content,

            "| CANAL:",

            message.channel.name

        )





        # Ignorar mensajes del bot

        if message.author.bot:

            return







        # Solo guardar mensajes de tickets

        if not message.channel.name.startswith(

            "ticket-"

        ):

            return





        print(

            "✅ PASÓ FILTRO DE TICKET"

        )








        # ==========================
        # ADJUNTOS
        # ==========================


        attachments = []



        for archivo in message.attachments:

            attachments.append(

                archivo.url

            )



        attachments_text = "\n".join(

            attachments

        )








        # ==========================
        # GUARDAR EVIDENCIA
        # ==========================


        try:


            print(

                "💾 Intentando guardar evidencia..."

            )



            db = conectar()

            cursor = db.cursor()



            cursor.execute(

                """

                INSERT INTO ticket_messages

                (

                    ticket_channel,

                    author,

                    author_id,

                    message,

                    attachments,

                    created_at

                )


                VALUES (?, ?, ?, ?, ?, ?)

                """,

                (

                    message.channel.name,

                    str(message.author),

                    str(message.author.id),

                    message.content,

                    attachments_text,

                    datetime.now().strftime(

                        "%Y-%m-%d %H:%M:%S"

                    )

                )

            )



            db.commit()

            db.close()





            print(

                f"📝 Evidencia guardada | {message.author} | {message.channel.name}"

            )





        except Exception as e:


            print(

                "❌ Error guardando evidencia:",

                e

            )









async def setup(bot):


    await bot.add_cog(

        MessageLogger(bot)

    )


    print(

        "✅ Message Logger cargado"

    )