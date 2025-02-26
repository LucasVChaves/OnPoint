import tkinter as tk
from tkinter import *
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente
from views.GUI import GUI
# Esse trem esquisito serve pra garantir esse
# arquivo como entrypoint
if __name__ == "__main__":
    app = GUI()  # Inicia a interface gráfica
    app.login_label()  # Executa a interface gráfica
