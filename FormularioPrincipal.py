#   importando tkinter
import tkinter as tk
from colores import (COLOR_MENU_CURSOR_ENCIMA, COLOR_CUERPO_PRINCIPAL,
                     COLOR_MENU_LATERAL, COLOR_BARRA_SUPERIOR)
import util.util_ventana as util_ventana
import util.util_imagen as util_imagen

#   instanciando una ventana principal
class FormularioPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        util_ventana.centrar_ventana(self, 1024, 600)
        self.logo = util_imagen.leer_imagen("./imgs/logoInstituto.png",(200,200))
        self.iconbitmap("./imgs/logoInstituto.png")