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
    
    def admin_login(self):
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
        admin.grid_rowconfigure(0, weight=0)  # Linha 0 com o header, não expansível
        admin.grid_rowconfigure(1, weight=1)  # Linha 1 expansível para o conteúdo abaixo do header
        admin.grid_columnconfigure(0, weight=1)  # Expansível horizontalmente

    # Coloca o header na linha 0
        HomeGUI.header(self.admin, admin, text="Área dos Administradores")  # Garante que o header seja posicionado na linha 0

    # Coloca o frame na linha 1, logo abaixo do header
        frame = Frame(admin, borderwidth=10)
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Configura o frame para ser expansível
        frame.grid_rowconfigure(0, weight=0)  # Linha para o título "Lista de Administradores"
        frame.grid_rowconfigure(1, weight=1)  # Linha para a Listbox expansível
        frame.grid_columnconfigure(0, weight=1)  # Expansível horizontalmente

    # Adiciona o título dentro do frame
        admLista = Label(frame, text="Lista de Administradores")
        admLista.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    # Adiciona a Listbox para mostrar os administradores
        administradores = Listbox(frame)
        administradores.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Inicia o loop principal
        admin.mainloop()


    def admin_interface(self):
        self.interf = tk.Tk()
        interf = self.interf

        # Chama o cabeçalho e o posiciona no topo
        HomeGUI.header(self.interf, interf, None)

        # Ajusta a geometria da janela
        scale_factor = 0.6
        screen_h = int(interf.winfo_screenheight() * scale_factor)
        screen_w = int(interf.winfo_screenwidth() * scale_factor)
        interf.geometry(f"{screen_w}x{screen_h}")

        # Configura a grade da janela principal
        interf.grid_rowconfigure(0, weight=0)  # Linha 0 com o header, não expansível
        interf.grid_rowconfigure(1, weight=1)  # Linha 1 expansível para o conteúdo
        interf.grid_rowconfigure(2, weight=2)  # Configura linha 2 para não expandir (caso necessário)
        interf.grid_columnconfigure(0, weight=1)  # Expansível horizontalmente

        # Coloca o header na linha 0
        HomeGUI.header(self.interf, interf, None)  # Garante que o header seja posicionado na linha 0

        # Coloca o frame na linha 1, logo abaixo do header
        frame = Frame(interf, borderwidth=10)
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  # Ocupa a linha 1

        # Configura o frame para ser expansível
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Inicia o loop principal
        interf.mainloop()
