from tkinter import *
from tkinter import ttk

class GUI():
    root = Tk() #cria janela raiz
    root.title("Home OnPoint")
    root.geometry('650x500') # Set geometry (widthxheight)

    labelForaTurno = Label(root, text="Fora do turno")
    labelEmTurno = Label(root, text="Em turno")

    labelForaTurno.grid(row=0, column=1)
    labelEmTurno.grid(row=0, column=2)
    
    homeBtn = Button(root, text="Home").grid(row=0, column=0)
    adminBtn = Button(root, text="Admin").grid(row=1, column=0)
    helpBtn = Button(root, text="Help").grid(row=3, column=0)
    root.mainloop()

