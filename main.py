import tkinter as tk
from tkinter import *
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente
from views.HomeGUI import HomeGUI

# Esse trem esquisito serve pra garantir esse
# arquivo como entrypoint
if __name__ == "__main__":
    app = HomeGUI()  # Inicia a interface gráfica
    app.home_label()  # Executa a interface gráfica
