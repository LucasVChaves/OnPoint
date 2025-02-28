import tkinter as tk
from tkinter import *
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente
from views.LoginGUI import LoginGUI
from views.HomeGUI import HomeGUI


# Esse trem esquisito serve pra garantir esse
# arquivo como entrypoint
if __name__ == "__main__":
    home = HomeGUI()
    home.home_label()
    #login = LoginGUI()
    #login.login_label()  # Inicia pelo login