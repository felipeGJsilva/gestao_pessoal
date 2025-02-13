import tkinter as tk
from tkinter import ttk

class FormularioBase(tk.Frame):
    def __init__(self, master, campos):
        super().__init__(master)
        self.campos = campos
        self.criar_formulario()

    def criar_formulario(self):
        for campo in self.campos:
            label = tk.Label(self, text=campo["label"])
            label.pack()
            if campo["tipo"] == "entry":
                entry = tk.Entry(self)
                entry.pack()
            elif campo["tipo"] == "combobox":
                combobox = ttk.Combobox(self, values=campo["opcoes"])
                combobox.pack()

    def validar(self):
        raise NotImplementedError("Método validar deve ser implementado.")