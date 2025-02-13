import tkinter as tk
from tkinter import messagebox

class LoginFrame(tk.Frame):
    def __init__(self, master, gerenciador_janelas):
        super().__init__(master)
        self.master = master
        self.gerenciador_janelas = gerenciador_janelas
        self.criar_widgets()

    def criar_widgets(self):
        # Campo de usuário
        tk.Label(self, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)

        # Campo de senha
        tk.Label(self, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_senha = tk.Entry(self, show="*")
        self.entry_senha.grid(row=1, column=1, padx=10, pady=10)

        # Botão de login
        tk.Button(self, text="Login", command=self.fazer_login).grid(row=2, column=1, padx=10, pady=10)

    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        # Lógica de autenticação (exemplo simples)
        if usuario == "admin" and senha == "admin":
            self.gerenciador_janelas.mostrar_frame("MenuPrincipal")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")