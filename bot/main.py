import discord

from discord.ext import commands

import asyncio

from db.database import crear_tablas

from config import TOKEN





# ==========================
# INTENTS
# ==========================

intents = discord.Intents.default()

intents.message_content = True

intents.members = True





# ==========================
# BOT
# ==========================

bot = commands.Bot(

    command_prefix="!",

    intents=intents

)





# ==========================
# CARGAR EXTENSIONES
# ==========================

async def cargar_extensiones():


    extensiones = [

        "commands.entregar",

        "commands.roblox",

        "commands.tickets",

        "events.message_logger"

    ]



    for extension in extensiones:


        try:


            await bot.load_extension(

                extension

            )


            print(

                f"✅ Cargado: {extension}"

            )



        except Exception as e:


            print(

                f"❌ Error cargando {extension}: {e}"

            )







# ==========================
# EVENTO ONLINE
# ==========================

@bot.event

async def on_ready():


    print("==============================")

    print("🤖 RobuxGuardian Bot Online")

    print("==============================")


    print(

        f"Conectado como: {bot.user}"

    )



    print(

        "📌 Comandos registrados:"

    )


    for comando in bot.tree.get_commands():

        print(

            f" /{comando.name}"

        )




    try:


        for guild in bot.guilds:


            # Eliminar comandos viejos del servidor

            bot.tree.clear_commands(

                guild=guild

            )



            await bot.tree.sync(

                guild=guild

            )



            # Copiar comandos actuales

            bot.tree.copy_global_to(

                guild=guild

            )



            synced = await bot.tree.sync(

                guild=guild

            )



            print(

                f"✅ Slash Commands sincronizados en {guild.name}: {len(synced)}"

            )



    except Exception as e:


        print(

            f"❌ Error sincronizando comandos: {e}"

        )







# ==========================
# INICIO
# ==========================

async def main():


    crear_tablas()



    print(

        "✅ Base de datos preparada"

    )



    await cargar_extensiones()



    await bot.start(

        TOKEN

    )








if __name__ == "__main__":


    asyncio.run(

        main()

    )