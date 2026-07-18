import discord

from services.risk import RiskSystem





def embed_analisis(usuario):


    try:

        analisis = RiskSystem.analizar(

            str(usuario.id)

        )


    except Exception as e:


        print(

            "❌ Error análisis usuario:",

            e

        )


        analisis = {


            "riesgo": 40,

            "nivel": "🟡 MEDIO",

            "texto": "No se pudo completar el análisis.",

            "robux": 0,

            "entregas": 0,

            "ultima": "Ninguna"

        }





    embed = discord.Embed(

        title="🛡️ RobuxGuardian | Análisis Automático",

        description="Análisis inicial realizado al crear el ticket.",

        color=0xF1C40F

    )





    embed.add_field(

        name="👤 Usuario",

        value=usuario.mention,

        inline=False

    )





    embed.add_field(

        name="⚠️ Riesgo",

        value=f"{analisis['nivel']} ({analisis['riesgo']}/100)",

        inline=True

    )





    embed.add_field(

        name="💎 Robux recibidos",

        value=f"{analisis.get('robux',0)} Robux",

        inline=True

    )





    embed.add_field(

        name="📦 Entregas",

        value=str(

            analisis.get(

                "entregas",

                0

            )

        ),

        inline=True

    )

    embed.add_field(

    name="🎟️ Tickets",

    value=str(

        analisis.get(

            "tickets",

            0

        )

    ),

    inline=True

)
    

    
    
    
    embed.add_field(
        
        name="📅 Última entrega",
        
        value=str(
            
            analisis.get(
                
                "ultima",
                
                "Ninguna"
                
            )
            
        ),
        
        inline=False
        
    )





    embed.add_field(

        name="📌 Resultado",

        value=analisis["texto"],

        inline=False

    )





    embed.set_footer(

        text="RobuxGuardian Enterprise Security"

    )


    return embed







def embed_verificacion(usuario):


    embed = discord.Embed(

        title="🎟️ RobuxGuardian | Verificación",

        description=f"""

Hola {usuario.mention} 👋


Para solicitar la revisión sigue estos pasos:


🎮 **Paso 1**

Envía tu usuario de Roblox.

Ejemplo:

`/roblox TU_USERNAME`

💎 **Paso 2**

El sistema revisará automáticamente tu historial.

📸 **Paso 3**

Si el staff necesita pruebas adicionales, envíalas dentro del ticket.


⚠️ **Reglas**
✅ Solo un ticket por persona.
✅ No hagas spam.
✅ Usa información real.
❌ Tickets falsos pueden recibir sanciones.



🛡️ RobuxGuardian está analizando tu solicitud.

""",

        color=0x5865F2

    )



    embed.set_footer(

        text="Sistema automático RobuxGuardian"

    )


    return embed