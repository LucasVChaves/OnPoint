from tkinter import *
import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from utils.JSONManager import JSONManager

from models.Employee import Employee
from models.Admin import Admin

from controllers.Login import Login

class GUI:
    def __init__(self):
        self.json_manager = JSONManager()
        self.login_class = Login()

        # Janelas
        self.login = None
        self.home = None
        pass

    # Frame para cabecalho
    # Add sempre quando for criar outra página
    # root é a janela, text é o texto do cabeçalho
    def header(self, root, text):
        # Criando um frame para o cabeçalho
        frame_cabecalho = tk.Frame(root, bg="navy", height=60)
        frame_cabecalho.pack(fill="x")

        label_titulo = tk.Label(frame_cabecalho, text=text,
                                font=("Arial", 16, "bold"), bg="navy", fg="white")
        label_titulo.pack(side="left", padx=10, pady=10)

        frame_botoes = tk.Frame(frame_cabecalho, bg="navy")
        frame_botoes.pack(side="right", padx=10)

        btn_sair = tk.Button(frame_botoes, text="❌ Sair", bg="red", fg="white", command=root.quit)
        btn_sair.pack(side="left", padx=5)



    # Função para a página inicial
    def home_label(self, user: any):
        self.home = tk.Tk()
        home = self.home

        home.title("OnPoint")
        home.geometry('650x500')

        self.header(root=home, text="OnPoint")
        home.mainloop()

