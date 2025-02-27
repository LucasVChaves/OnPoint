from tkinter import *
import tkinter as tk
from tkinter import Listbox, Label, Frame
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from utils.JSONManager import JSONManager

from models.Employee import Employee
from models.Admin import Admin

from controllers.Login import Login

class HomeGUI:
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

    def update_clock(self, label):
        curr_time = datetime.now().strftime("%H:%M:%S")
        label.config(text=curr_time)
        label.after(1000, self.update_clock, label)

    def clock(self, root):
        frame_clock = tk.Frame(root, height=150)
        frame_clock.grid(row=1, column=0, sticky="ew")
        frame_clock.grid_propagate(False)

        label_clock = tk.Label(frame_clock, text='clock', font=("Arial", 20, "bold"))
        label_clock.grid(row=0, column=0, sticky="ew")
        self.update_clock(label_clock)
        frame_clock.grid_rowconfigure(0, weight=1)
        frame_clock.grid_columnconfigure(0, weight=1)

        today = datetime.now().strftime("%d/%m/%Y - %A")
        label_date = tk.Label(frame_clock, text=today, font=("Arial", 15, "italic"))
        label_date.grid(row=1, column=0, sticky="ew")
        frame_clock.grid_rowconfigure(1, weight=1)

    # Função para a página inicial
    def home_label(self):
        self.home = tk.Tk()
        home = self.home

        home.title("OnPoint")

        scale_factor = 0.6
        screen_h = int(home.winfo_screenheight() * scale_factor)
        screen_w = int(home.winfo_screenwidth() * scale_factor)

        home.geometry(f"{screen_w}x{screen_h}")
        home.grid_rowconfigure(0, weight=2)
        home.grid_rowconfigure(1, weight=1)
        home.grid_rowconfigure(2, weight=2)
        home.grid_columnconfigure(0, weight=1)

        # Adicionando um frame principal
        frame = Frame(home, borderwidth=10)
        frame.pack(expand=True, fill="both")
        frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Chamando o cabeçalho e colocando-o acima das Listbox
        self.header(root=home, text="OnPoint")

        # Chama label do relogio
        self.clock(root=home)

        # Criando as Labels
        foraTurnoLabel = Label(frame, text="Fora de Turno", background='#ff5757')
        emTurnoLabel = Label(frame, text="Em turno", background='#00bf63')
        
        # Criando as Listbox
        #TODO:  fazer as listboxes serem listas de botoes
        #cada botao vai ter o nome do funcionario/admin
        #a ação do click do botao roda a tela de login
        foraTurnoListbox = Listbox(frame)
        emTurnoListbox = Listbox(frame)

        # Exibindo as Labels
        foraTurnoLabel.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        emTurnoLabel.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

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

