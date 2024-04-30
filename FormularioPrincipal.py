#   importando tkinter
import requests
import tkinter as tk
from tkinter import Label, Entry, Button
from Api.GestionApi import imprimir_respuesta
from colores import (COLOR_MENU_CURSOR_ENCIMA, COLOR_CUERPO_PRINCIPAL,
                     COLOR_MENU_LATERAL, COLOR_BARRA_SUPERIOR)
import util.util_ventana as util_ventana
import util.util_imagen as util_imagen


#   instanciando una ventana principal
class FormularioPrincipal(tk.Tk):

    def __init__(self):   # constructor
        super().__init__()
        util_ventana.centrar_ventana(self, 1024, 600)
        self.nombre=tk.StringVar(self)
        self.artista=tk.StringVar(self)
        self.album=tk.StringVar(self)
        self.lanzamiento=tk.StringVar(self)
        self.genero=tk.StringVar(self)
        self.letra=tk.StringVar(self)

    def cargarCancion(self):
        urlApi = "https://biblioisp20-92ed.restdb.io/rest/canciones?apikey=2c677ccf2cb62a940092248e128001983dab0"

        cancion = {
            "nombre": self.nombre.get(),
            "artista": self.artista.get(),
            "album": self.album.get(),
            "lanzamiento": 2000,
            "genero": self.genero.get(),
            "letra": self.letra.get()
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        respuesta = requests.request("POST", urlApi, headers=headers, data=cancion)
        imprimir_respuesta(respuesta)
    def colocarControlesEnPantalla(self):
        Label(self, text="Nombre:").grid(pady=5, row=0, column=0)
        Label(self, text="Artista:").grid(pady=5, row=1, column=0)
        Label(self, text="Album:").grid(pady=5, row=2, column=0)
        Label(self, text="Lanzamiento:").grid(pady=5, row=3, column=0)
        Label(self, text="Genero:").grid(pady=5, row=4, column=0)
        Label(self, text="Letra:").grid(pady=5, row=5, column=0)

        Entry(self, textvariable=self.nombre, width=100).grid(padx=5, row=0, column=1)
        Entry(self, textvariable=self.artista, width=100).grid(padx=5, row=1, column=1)
        Entry(self, textvariable=self.album, width=100).grid(padx=5, row=2, column=1)
        Entry(self, textvariable=self.lanzamiento, width=100).grid(padx=5, row=3, column=1)
        Entry(self, textvariable=self.genero, width=100).grid(padx=5, row=4, column=1)
        Entry(self, textvariable=self.letra, width=100).grid(padx=5, row=5, column=1)

        Button(self, text="Aceptar", command=self.cargarCancion, width=100).grid(padx=20,
                                                     pady=20,
                                                     row=6,
                                                     column=0,
                                                     columnspan=2)
