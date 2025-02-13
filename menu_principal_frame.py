import tkinter as tk

class MenuPrincipalFrame(tk.Frame):
    def __init__(self, master, gerenciador_janelas):
        super().__init__(master)
        self.master = master
        self.gerenciador_janelas = gerenciador_janelas
        self.criar_widgets()

    def criar_widgets(self):
        # Título do menu principal
        tk.Label(self, text="Menu Principal", font=("Arial", 24)).pack(pady=20)

        # Botão para voltar ao login
        tk.Button(self, text="Voltar para o Login", command=self.voltar_login).pack(pady=10)

    def voltar_login(self):
        self.gerenciador_janelas.mostrar_frame("Login")