from tkinter import *
import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona dinamicamente

from utils.JSONManager import JSONManager

from models.Employee import Employee
from models.Admin import Admin

class AdminGUI:
    def __init__(self):
        print("sua mae")