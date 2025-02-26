import tkinter as tk
from tkinter import ttk
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente
from utils.JSONManager import JSONManager

class GUI:
    def __init__(self):
        self.jsonManager = JSONManager()

        # Janelas
        self.login = None
        self.home = None
        pass

    # Frame para cabecalho
    # Add sempre quando for criar outra página
    def cabecalho(self, root, text):
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

    def login_aux(self, id, PIN):
        if self.jsonManager.load_from_json('employee', id)['PIN'] == PIN:
            self.login.destroy()
            self.home_label()

        else:
            label_erro = tk.Label(self.login, text="ID ou PIN incorretos", fg="red")
            label_erro.pack()
            raise ValueError("ID ou PIN incorretos")

    def login_label(self):
        # Login
        self.login = tk.Tk()
        login = self.login

        login.title("Login OnPoint")
        login.geometry('650x500')

        self.cabecalho(root=login, text="Login OnPoint")

        # Criando um frame para o formulário
        frame_formulario = tk.Frame(login, bg="white")
        frame_formulario.pack(pady=50)

        # Agora usamos grid() APENAS dentro do frame_formulario
        tk.Label(frame_formulario, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        entrada_ID = tk.Entry(frame_formulario)
        entrada_ID.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_formulario, text="PIN:").grid(row=1, column=0, padx=5, pady=5)
        entrada_PIN = tk.Entry(frame_formulario)
        entrada_PIN.grid(row=1, column=1, padx=5, pady=5)

        botao = tk.Button(frame_formulario, text="Enviar", command=lambda: self.login_aux(entrada_ID.get(), entrada_PIN.get()))
        botao.grid(row=2, columnspan=2, pady=10)

        login.mainloop()

    def home_label(self):
        self.home = tk.Tk()
        home = self.home

        home.title("OnPoint")
        home.geometry('650x500')

        self.cabecalho(root=home, text="OnPoint")
        pass



    # # Criando o cabeçalho
    # cabecalho = tk.Label(root, text="OnPoint", 
    #                     font=("Arial", 14, "bold"),  # Fonte grande e negrito
    #                     bg="blue", fg="white",  # Fundo azul e texto branco
    #                     padx=10, pady=10)  # Espaçamento interno
    # cabecalho.pack(fill="x")  # Expande o cabeçalho horizontalmente

    # labelForaTurno = Label(root, text="Fora do turno")
    # labelEmTurno = Label(root, text="Em turno")

    # labelForaTurno.grid(row=0, column=1)
    # labelEmTurno.grid(row=0, column=2)
    
    # homeBtn = Button(root, text="Home").grid(row=0, column=0)
    # adminBtn = Button(root, text="Admin").grid(row=1, column=0)
    # helpBtn = Button(root, text="Help").grid(row=3, column=0)

