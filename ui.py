from tkinter import *
from tkinter import ttk

class Ui:
    def __init__(self, root) -> None:
        root.title("Scrabble helper")

        mainframe = ttk.Frame(root, padding="5 5 5 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.button_pressed=StringVar()
        self.search_button = ttk.Button(mainframe, text='Search',command=lambda: self.button_pressed.set("button pressed"))
        self.search_button.grid(column=2, row=1)

        self.length_entry = ttk.Entry(mainframe)
        self.length_entry.grid(column=1, row=1)

        self.restr_entry = ttk.Entry(mainframe)
        self.restr_entry.grid(column=1, row=2)

        self.results = StringVar()
        self.outp_label = ttk.Label(mainframe,textvariable=self.results)
        self.outp_label.grid(column=2,row=2)

    def get_length(self):
        return self.length_entry.get()

    def get_restr(self):
        return self.restr_entry.get()

    def wait_button_pressed(self):
        if self.search_button.wait_variable(self.button_pressed):
            return None
    
    def set_label(self,content):
        self.results.set(content)



