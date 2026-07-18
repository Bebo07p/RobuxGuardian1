import requests

from datetime import datetime



class RobloxAPI:


    BASE = "https://users.roblox.com/v1"

    THUMBNAILS = "https://thumbnails.roblox.com/v1"





    @staticmethod
    def buscar_usuario(username: str):

        try:

            r = requests.post(

                f"{RobloxAPI.BASE}/usernames/users",

                json={

                    "usernames": [

                        username

                    ],

                    "excludeBannedUsers": False

                },

                timeout=10

            )


            if r.status_code != 200:

                return None



            data = r.json()



            if not data.get("data"):

                return None



            return data["data"][0]



        except Exception as e:

            print(

                "❌ Error buscando usuario Roblox:",

                e

            )

            return None







    @staticmethod
    def obtener_informacion(user_id):

        try:

            r = requests.get(

                f"{RobloxAPI.BASE}/users/{user_id}",

                timeout=10

            )


            if r.status_code != 200:

                return None



            return r.json()



        except Exception as e:

            print(

                "❌ Error obteniendo información Roblox:",

                e

            )

            return None







    @staticmethod
    def obtener_avatar(user_id):

        try:

            r = requests.get(

                f"{RobloxAPI.THUMBNAILS}/users/avatar-headshot",

                params={

                    "userIds": user_id,

                    "size": "420x420",

                    "format": "Png",

                    "isCircular": False

                },

                timeout=10

            )


            data = r.json()



            if not data.get("data"):

                return None



            return data["data"][0]["imageUrl"]



        except Exception as e:

            print(

                "❌ Error obteniendo avatar:",

                e

            )

            return None







    @staticmethod
    def calcular_edad(created):

        try:

            fecha = datetime.fromisoformat(

                created.replace(

                    "Z",

                    "+00:00"

                )

            )


            hoy = datetime.now(

                fecha.tzinfo

            )


            años = hoy.year - fecha.year



            if (

                hoy.month,

                hoy.day

            ) < (

                fecha.month,

                fecha.day

            ):

                años -= 1



            return años



        except Exception as e:

            print(

                "❌ Error calculando edad:",

                e

            )

            return 0