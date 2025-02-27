from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from models.Employee import Employee
from models.Schedules import Schedules
from models.Role import Role
from utils.JSONManager import JSONManager
from utils.IDGen import IDGen

from views.HomeGUI import HomeGUI

class CadastreGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Usuários")

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        self.create_widgets()

    def create_widgets(self):
        
        HomeGUI.header(self.master, self.master, text="Área dos Administradores")

        # Labels e Entradas para os dados do usuário
        self.lbl_pin = Label(self.master, text="PIN")
        self.lbl_pin.grid(row=1, column=0, padx=10, pady=10)
        self.ent_pin = Entry(self.master)
        self.ent_pin.grid(row=1, column=1, padx=10, pady=10)
        
        self.lbl_name = Label(self.master, text="Nome")
        self.lbl_name.grid(row=2, column=0, padx=10, pady=10)
        self.ent_name = Entry(self.master)
        self.ent_name.grid(row=2, column=1, padx=10, pady=10)
        
        self.lbl_email = Label(self.master, text="Email")
        self.lbl_email.grid(row=3, column=0, padx=10, pady=10)
        self.ent_email = Entry(self.master)
        self.ent_email.grid(row=3, column=1, padx=10, pady=10)
        
        self.lbl_phone = Label(self.master, text="Telefone")
        self.lbl_phone.grid(row=4, column=0, padx=10, pady=10)
        self.ent_phone = Entry(self.master)
        self.ent_phone.grid(row=4, column=1, padx=10, pady=10)
        
        self.lbl_address = Label(self.master, text="Endereço")
        self.lbl_address.grid(row=5, column=0, padx=10, pady=10)
        self.ent_address = Entry(self.master)
        self.ent_address.grid(row=5, column=1, padx=10, pady=10)
        
        self.lbl_birth = Label(self.master, text="Data de Nascimento (AAAA-MM-DD)")
        self.lbl_birth.grid(row=6, column=0, padx=10, pady=10)
        self.ent_birth = Entry(self.master)
        self.ent_birth.grid(row=6, column=1, padx=10, pady=10)
        
        self.lbl_salary = Label(self.master, text="Salário")
        self.lbl_salary.grid(row=7, column=0, padx=10, pady=10)
        self.ent_salary = Entry(self.master)
        self.ent_salary.grid(row=7, column=1, padx=10, pady=10)

        self.lbl_role = Label(self.master, text="Cargo")
        self.lbl_role.grid(row=8, column=0, padx=10, pady=10)

        vlist = ["ADMIN", "EMPLOYEE"]

        combo = ttk.Combobox(self.master, values = vlist)
        combo.grid(row=8, column=1, padx=10, pady=10)
        
        # Botão de Cadastro
        self.btn_register = Button(self.master, text="Cadastrar", command=self.register_user)
        self.btn_register.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
        
    def register_user(self):
        pin = self.ent_pin.get()
        name = self.ent_name.get()
        email = self.ent_email.get()
        phone = self.ent_phone.get()
        address = self.ent_address.get()
        birth = self.ent_birth.get()
        salary = self.ent_salary.get()
        role = self.ent_role.get()

        # Convertendo a data de nascimento e o salário
        try:
            birth = datetime.strptime(birth, "%Y-%m-%d")
            salary = float(salary)
        except ValueError as e:
            messagebox.showerror("Erro", f"Erro ao converter dados: {e}")
            return
        
        schedules = Schedules()  # Supondo que Schedules seja configurado de outra maneira
        
        role = Role.ADMIN if role.upper() == "ADMIN" else Role.EMPLOYEE
        
        cadastre = Cadastre()
        
        if cadastre.cadastre_user(pin, name, email, phone, address, birth, salary, schedules, role):
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Erro ao cadastrar usuário!")

'''if __name__ == "__main__":
    root = tk.Tk()
    app = CadastreGUI(master=root)
    root.mainloop()'''
