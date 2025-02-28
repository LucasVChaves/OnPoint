from tkinter import *
import tkinter as tk
from tkinter import Listbox, Label, Frame, messagebox
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from utils.JSONManager import JSONManager
from models.Employee import Employee
from models.Admin import Admin
from controllers.Login import Login
from models.Clock import Clock  # Importação correta
from utils.State import State

class HomeGUI:
    def __init__(self):
        self.home = None
        self.json_manager = JSONManager()  # Inicializa JSONManager para carregar funcionários
        self.foraTurnoListbox = None
        self.emTurnoListbox = None
        self.usuario_logado = None  # Para armazenar o usuário logado

    # Frame para cabeçalho
    def header(self, root, text):
        frame_cabecalho = tk.Frame(root, bg="navy", height=60)
        frame_cabecalho.grid(row=0, column=0, columnspan=2, sticky="ew")

        label_titulo = tk.Label(frame_cabecalho, text=text,
                                font=("Arial", 16, "bold"), bg="navy", fg="white")
        label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        frame_botoes = tk.Frame(frame_cabecalho, bg="navy")
        frame_botoes.grid(row=0, column=1, padx=10, sticky="e")

        btn_sair = tk.Button(frame_botoes, text="❌ Sair", bg="red", fg="white", command=root.quit)
        btn_sair.grid(row=0, column=0, padx=5)

    # Atualiza o relógio
    def update_clock(self, label):
        curr_time = datetime.now().strftime("%H:%M:%S")
        label.config(text=curr_time)
        label.after(1000, self.update_clock, label)

    # Exibe o relógio
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

    # Atualiza a lista de funcionários na interface
    def update_employee_lists(self):
        employees_data = self.json_manager.load_all_from_json('employee')

        self.foraTurnoListbox.delete(0, tk.END)
        self.emTurnoListbox.delete(0, tk.END)

        if employees_data:
            for emp in employees_data:
                # Usando o valor do enum 'State' diretamente para verificar o estado
                if emp.get("state") == State.WORKING.value:  # Verificando o valor do estado
                    self.emTurnoListbox.insert(tk.END, emp["name"])
                else:
                    self.foraTurnoListbox.insert(tk.END, emp["name"])

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

        # Chama label do relógio
        self.clock(root=home)

        # Criando as Labels
        foraTurnoLabel = Label(frame, text="Fora de Turno", background='#ff5757')
        emTurnoLabel = Label(frame, text="Em turno", background='#00bf63')

        # Criando as Listbox
        self.foraTurnoListbox = Listbox(frame)
        self.emTurnoListbox = Listbox(frame)

        # Exibindo as Labels
        foraTurnoLabel.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        emTurnoLabel.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Exibindo as Listboxes
        self.foraTurnoListbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.emTurnoListbox.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Criando um frame para os botões
        frame_botoes = tk.Frame(home)
        frame_botoes.grid(row=3, column=0, columnspan=2, pady=10)

        # Botão de bater ponto
        btn_bater_ponto = tk.Button(frame_botoes, text="Bater Ponto", command=self.abrir_clock)
        btn_bater_ponto.pack(side=tk.LEFT, padx=10)

        # Botão de justificar ponto
        btn_justificar = tk.Button(frame_botoes, text="Justificar Frequência", command=self.abrir_justificativa)
        btn_justificar.pack(side=tk.LEFT, padx=10)

        # Botão de administração (visível apenas para admins)
        if self.usuario_logado and self.usuario_logado.role == "Admin":
            btn_admin = tk.Button(frame_botoes, text="Área do Admin", command=self.abrir_admin)
            btn_admin.pack(side=tk.LEFT, padx=10)

        # Configuração do grid para as colunas se expandirem
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        # Atualizar listas de funcionários ao abrir a tela
        self.update_employee_lists()

        home.mainloop()

    # Função corrigida para "Bater Ponto"
    def abrir_clock(self):
        """ Função acionada pelo botão "Bater Ponto". """
        if self.usuario_logado:
            employee_id = self.usuario_logado.get_id()  # Garantindo que o ID correto está sendo usado
            state = self.usuario_logado.get_state()  # ✅ Certificando que o estado está correto também

            try:
                clock = Clock()
                clock.action_clock(employee_id, state)  # Registra o ponto corretamente
                messagebox.showinfo("Sucesso", "Ponto registrado com sucesso!")
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showwarning("Aviso", "Nenhum usuário logado!")

    # Funções para abrir outras telas
    def abrir_justificativa(self):
        from views.JustificativaGUI import JustificativaGUI  # Importação atrasada
        justificativa = JustificativaGUI()
        justificativa.justificativa_label()

    def abrir_admin(self):
        from views.AdminGUI import AdminGUI  # Importação atrasada
        admin = AdminGUI()
        admin.admin_interface()
