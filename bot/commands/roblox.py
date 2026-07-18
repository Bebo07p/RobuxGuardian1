import discord

from discord.ext import commands

from db.database import conectar

from services.roblox_api import RobloxAPI

from discord import app_commands




class Roblox(commands.Cog):


    def __init__(self, bot):

        self.bot = bot







    @discord.app_commands.command(

        name="roblox",

        description="Consulta información de un usuario de Roblox"

    )

    async def roblox(

        self,

        interaction: discord.Interaction,

        username: str

    ):


        await interaction.response.defer()





        try:


            # ==========================
            # BUSCAR USUARIO
            # ==========================


            usuario = RobloxAPI.buscar_usuario(

                username

            )



            if usuario is None:


                return await interaction.followup.send(

                    "❌ Ese usuario de Roblox no existe."

                )





            # ==========================
            # INFORMACION ROBLOX
            # ==========================


            info = RobloxAPI.obtener_informacion(

                usuario["id"]

            )



            if info is None:


                return await interaction.followup.send(

                    "❌ No se pudo obtener la información de Roblox."

                )




            avatar = RobloxAPI.obtener_avatar(

                usuario["id"]

            )



            descripcion = info.get(

                "description",

                "Sin descripción."

            )



            creada = info.get(

                "created",

                "Desconocida"

            )



            edad = RobloxAPI.calcular_edad(

                creada

            )



            baneado = (

                "Sí 🔴"

                if info.get("isBanned", False)

                else

                "No 🟢"

            )



            perfil = (

                f"https://www.roblox.com/users/{usuario['id']}/profile"

            )






            # ==========================
            # DATABASE
            # ==========================


            db = conectar()

            cursor = db.cursor()



            cursor.execute("""

            CREATE TABLE IF NOT EXISTS roblox_accounts(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                discord_id TEXT UNIQUE,

                discord_username TEXT,

                roblox_id TEXT,

                roblox_username TEXT,

                display_name TEXT,

                description TEXT,

                avatar TEXT,

                created TEXT,

                verified INTEGER DEFAULT 1

            )

            """)




            cursor.execute("""

            INSERT OR REPLACE INTO roblox_accounts(

                discord_id,

                discord_username,

                roblox_id,

                roblox_username,

                display_name,

                description,

                avatar,

                created,

                verified

            )

            VALUES(?,?,?,?,?,?,?,?,?)

            """,(


                str(interaction.user.id),

                str(interaction.user),

                str(usuario["id"]),

                usuario["name"],

                usuario["displayName"],

                descripcion,

                avatar,

                creada,

                1


            ))



            db.commit()

            db.close()








            # ==========================
            # EMBED
            # ==========================


            embed = discord.Embed(

                title="🛡️ RobuxGuardian | Usuario Roblox",

                color=0x00b0f4

            )



            embed.add_field(

                name="👤 Discord",

                value=interaction.user.mention,

                inline=False

            )



            embed.add_field(

                name="🎮 Usuario",

                value=usuario["name"],

                inline=True

            )



            embed.add_field(

                name="🏷 Display Name",

                value=usuario["displayName"],

                inline=True

            )



            embed.add_field(

                name="🆔 Roblox ID",

                value=str(usuario["id"]),

                inline=False

            )



            embed.add_field(

                name="📅 Cuenta creada",

                value=creada[:10],

                inline=True

            )



            embed.add_field(

                name="⌛ Edad",

                value=f"{edad} años",

                inline=True

            )



            embed.add_field(

                name="🚫 Baneado",

                value=baneado,

                inline=True

            )



            embed.add_field(

                name="📝 Descripción",

                value=descripcion[:1000],

                inline=False

            )



            embed.add_field(

                name="🔗 Perfil",

                value=f"[Abrir Perfil]({perfil})",

                inline=False

            )



            embed.add_field(

                name="🛡️ Estado",

                value="✅ Usuario verificado mediante la API oficial de Roblox.",

                inline=False

            )



            if avatar:

                embed.set_thumbnail(

                    url=avatar

                )



            embed.set_footer(

                text="RobuxGuardian Security System"

            )




            await interaction.followup.send(

                embed=embed

            )



        except Exception as e:


            print(

                "❌ Error comando roblox:",

                e

            )


            await interaction.followup.send(

                "❌ Ocurrió un error procesando el usuario."

            )









async def setup(bot):


    await bot.add_cog(

        Roblox(bot)

    )


    print(

        "✅ Roblox cargado"

    )