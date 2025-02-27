from tkinter import *
import tkinter as tk
from tkinter import Listbox, Label, Frame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from utils.JSONManager import JSONManager

from models.Employee import Employee
from models.Admin import Admin

from controllers.Login import Login

class GUI:
    def __init__(self):
        self.home = None

        # Janelas
        '''self.login = None
        self.home = None
        pass'''

    
    # Frame para cabecalho
    # Add sempre quando for criar outra página
    # root é a janela, text é o texto do cabeçalho
    def header(self, root, text):
        # Criando um frame para o cabeçalho
        frame_cabecalho = tk.Frame(root, bg="navy", height=60)
        frame_cabecalho.grid(row=0, column=0, columnspan=2, sticky="ew")

        label_titulo = tk.Label(frame_cabecalho, text=text,
                                font=("Arial", 16, "bold"), bg="navy", fg="white")
        label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        frame_botoes = tk.Frame(frame_cabecalho, bg="navy")
        frame_botoes.grid(row=0, column=1, padx=10, sticky="e")

        btn_sair = tk.Button(frame_botoes, text="❌ Sair", bg="red", fg="white", command=root.quit)
        btn_sair.grid(row=0, column=0, padx=5)



    # Função para a página inicial
    def home_label(self):
        self.home = tk.Tk()
        home = self.home

        home.title("OnPoint")


        # Adicionando um frame principal
        frame = Frame(home)
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Chamando o cabeçalho e colocando-o acima das Listbox
        self.header(root=home, text="OnPoint")

        # Criando as Labels
        foraTurnoLabel = Label(frame, text="Fora de Turno")
        emTurnoLabel = Label(frame, text="Em turno")
        
        # Criando as Listbox
        foraTurnoListbox = Listbox(frame)
        emTurnoListbox = Listbox(frame)

        # Exibindo as Labels
        foraTurnoLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        emTurnoLabel.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Exibindo as Listboxes
        foraTurnoListbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        emTurnoListbox.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Configuração do grid para as colunas se expandirem
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        # Configuração do grid para a linha 0 se expandir (para o cabeçalho)
        home.grid_rowconfigure(0, weight=0)  # Cabeçalho não expande
        home.grid_rowconfigure(1, weight=1)  # Área de conteúdo expande

        home.mainloop()

