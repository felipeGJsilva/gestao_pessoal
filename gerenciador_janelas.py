import tkinter as tk

class GerenciadorJanelas:
    def __init__(self, root):
        self.root = root
        self.frames = {}
        self.frame_atual = None

    def adicionar_frame(self, nome, frame_class):
        frame = frame_class(self.root, self)
        self.frames[nome] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_remove()

    def mostrar_frame(self, nome):
        if self.frame_atual:
            self.frame_atual.grid_remove()
        self.frame_atual = self.frames[nome]
        self.frame_atual.grid()
        self.frame_atual.tkraise()