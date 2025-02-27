from tkinter import *
import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from utils.JSONManager import JSONManager

from models.Employee import Employee
from models.Admin import Admin

from controllers.Login import Login


class LoginGUI():
    def __init__(self):
        self.json_manager = JSONManager()
        self.login_class = Login()
    # Função auxiliar para login
    # id é o ID do funcionário, PIN é o PIN
    def login_aux(self, id, PIN):
        if not self.login_class.action_login(id, PIN):
            label_erro = tk.Label(self.login, text="ID ou PIN incorretos", fg="red")
            label_erro.pack()
        else:
            # Fecha janela de login
            self.login.destroy()

            self.home_label(self.login_class.action_login(id, PIN))

    # Função para a página de login
    def login_label(self):
        # Login
        self.login = tk.Tk()
        login = self.login

        login.title("Login OnPoint")
        login.geometry('650x500')

        self.header(root=login, text="Login OnPoint")

        # Criando um frame para o formulário
        frame_formulario = tk.Frame(login, bg="white")
        frame_formulario.pack(pady=50)

        # Campos do formulário
        tk.Label(frame_formulario, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        entrada_ID = tk.Entry(frame_formulario)
        entrada_ID.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_formulario, text="PIN:").grid(row=1, column=0, padx=5, pady=5)
        entrada_PIN = tk.Entry(frame_formulario)
        entrada_PIN.grid(row=1, column=1, padx=5, pady=5)

        botao = tk.Button(frame_formulario, text="Enviar", command=lambda: self.login_aux(entrada_ID.get(), entrada_PIN.get()))
        botao.grid(row=2, columnspan=2, pady=10)

        login.mainloop()
