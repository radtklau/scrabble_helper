from tkinter import *
from tkinter import ttk

class Ui:
    def __init__(self,root) -> None:
        root.title("Scrabble helper")

        mainframe = ttk.Frame(root, padding="5 5 5 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        search_button = ttk.Button(mainframe)
        search_button.grid(column=3, row=2)