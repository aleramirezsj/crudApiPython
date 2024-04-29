import requests
import json

base_url = "https://biblioisp20-92ed.restdb.io/rest/canciones?apikey=2c677ccf2cb62a940092248e128001983dab0"


def imprimir_respuesta(respuesta):
    print(respuesta.text)
    print(respuesta.json())
    print(respuesta.status_code)
    print(respuesta.headers)
def crear_cancion():

    cancion = {
        "nombre": "Claro oscuro",
        "artista": "La vela puerca",
        "album": "A contra luz",
        "lanzamiento": 2004,
        "genero": "rock",
        "letra": "algo oscuro te hace pensar y eso no corresponde"
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    respuesta = requests.request("POST", base_url, headers=headers, data=cancion)
    imprimir_respuesta(respuesta)



crear_cancion()
