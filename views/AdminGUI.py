from tkinter import *
import tkinter as tk
import sys
import os

utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils'))
sys.path.append(utils_path)

from utils.JSONManager import JSONManager

from models.Employee import Employee
from models.Admin import Admin

from views.HomeGUI import HomeGUI

class AdminGUI:
    def __init__(self):
        self.admin = None
    
    def admin_label(self):
        self.admin = tk.Tk()
        admin = self.admin

        # Chama o cabeçalho e o posiciona no topo
        HomeGUI.header(self.admin, admin, text="Área dos Administradores")

        # Ajusta a geometria da janela
        scale_factor = 0.6
        screen_h = int(admin.winfo_screenheight() * scale_factor)
        screen_w = int(admin.winfo_screenwidth() * scale_factor)
        admin.geometry(f"{screen_w}x{screen_h}")

        # Configura a grade da janela principal
        admin.grid_rowconfigure(0, weight=0)  # Não expande o header
        admin.grid_rowconfigure(1, weight=1)  # Expande o conteúdo abaixo do header
        admin.grid_columnconfigure(0, weight=1)  # Expande a coluna

        # Coloca o frame na linha 1, logo abaixo do header
        frame = Frame(admin, borderwidth=10)
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Configura o frame para ser expansível
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        admLista = Label(frame, text="Lista de Adiministradores")
        admLista.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        administradores = Listbox(frame)
        administradores.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        admin.mainloop()

