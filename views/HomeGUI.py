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
                self.foraTurnoListbox.insert(tk.END, emp["name"])  # Exibe todos os funcionários, sem validar o estado

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
            btn_admin = tk.Button(frame_botoes, text="Admin", command=self.abrir_admin)
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
            # Agora, o estado é passado diretamente ao clicar no botão de bater ponto
            state = State.WORKING  # Definido diretamente como "Working" para o exemplo, se necessário
            try:
                clock = Clock()
                clock.action_clock(employee_id, state)  # Registra o ponto corretamente
                messagebox.showinfo("Sucesso", "Ponto registrado com sucesso!")
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showwarning("Aviso", "Nenhum usuário logado!")

    # Função para abrir a tela de Justificativa de Frequência
    def abrir_justificativa(self):
        justificativa = tk.Toplevel(self.home)  # Cria uma nova janela
        justificativa.title("Justificar Frequência")

        # Label para instrução
        label = Label(justificativa, text="Digite a justificativa para sua ausência:")
        label.pack(pady=10)

        # Campo de texto para justificar
        justificativa_text = Text(justificativa, height=10, width=40)
        justificativa_text.pack(padx=10, pady=10)

        # Botões de Enviar e Voltar
        btn_enviar = Button(justificativa, text="Enviar", command=lambda: self.enviar_justificativa(justificativa_text))
        btn_enviar.pack(side=tk.LEFT, padx=10, pady=10)

        btn_voltar = Button(justificativa, text="Voltar", command=justificativa.destroy)
        btn_voltar.pack(side=tk.RIGHT, padx=10, pady=10)

    # Função para enviar a justificativa (aqui você pode adicionar o que deve ser feito com a justificativa)
    def enviar_justificativa(self, justificativa_text):
        justificativa = justificativa_text.get("1.0", "end-1c")  # Captura o texto digitado
        if justificativa.strip() == "":  # Verifica se não foi digitado nada
            messagebox.showwarning("Aviso", "Por favor, digite uma justificativa.")
        else:
            # Aqui você pode fazer o que for necessário com a justificativa
            messagebox.showinfo("Sucesso", "Justificativa enviada com sucesso!")

    # Função para abrir a tela de Admin
    def abrir_admin(self):
        from views.AdminGUI import AdminGUI  # Importação da tela de admin
        admin = AdminGUI()  # Criação da instância da tela AdminGUI
        admin.admin_interface()  # Chama o método para exibir a interface de admin
