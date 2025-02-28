from tkinter import *
import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from utils.JSONManager import JSONManager
from models.Employee import Employee
from models.Admin import Admin
from controllers.Login import Login
from views.HomeGUI import HomeGUI  # Importação atrasada para abrir a tela principal

class LoginGUI:
    def __init__(self):
        self.json_manager = JSONManager()
        self.login_class = Login()
        
    # Função auxiliar para login
    def login_aux(self, id, PIN):
        try:
            user = self.login_class.action_login(id, PIN)  # Retorna um objeto Employee ou Admin
            if user:
                self.login.destroy()  # Fecha janela de login
                home = HomeGUI()
                home.usuario_logado = user  # Passa o usuário logado para a home
                home.home_label()
            else:
                label_erro = tk.Label(self.login, text="ID ou PIN incorretos", fg="red")
                label_erro.pack()
        except ValueError as e:
            label_erro = tk.Label(self.login, text=str(e), fg="red")
            label_erro.pack()

    # Função para a página de login
    def login_label(self):
        # Criando a janela de login
        self.login = tk.Tk()
        login = self.login

        login.title("Login OnPoint")
        login.geometry('650x500')

        # Criando um cabeçalho (corrigindo a chamada de `self.header`)
        label_titulo = tk.Label(login, text="Login OnPoint",
                                font=("Arial", 16, "bold"), bg="navy", fg="white")
        label_titulo.pack(pady=10, fill="x")

        # Criando um frame para o formulário
        frame_formulario = tk.Frame(login, bg="white")
        frame_formulario.pack(pady=50)

        # Campos do formulário
        tk.Label(frame_formulario, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        entrada_ID = tk.Entry(frame_formulario)
        entrada_ID.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_formulario, text="PIN:").grid(row=1, column=0, padx=5, pady=5)
        entrada_PIN = tk.Entry(frame_formulario, show="*")  # Esconde o PIN por segurança
        entrada_PIN.grid(row=1, column=1, padx=5, pady=5)

        # Botão de Login
        botao = tk.Button(frame_formulario, text="Enviar", 
                            command=lambda: self.login_aux(entrada_ID.get(), entrada_PIN.get()))
        botao.grid(row=2, columnspan=2, pady=10)

        login.mainloop()
