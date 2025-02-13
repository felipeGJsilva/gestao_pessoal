import tkinter as tk
from gerenciador_janelas import GerenciadorJanelas
from login_frame import LoginFrame
from menu_principal_frame import MenuPrincipalFrame

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão de Pessoal")
        self.geometry("1024x768")

        # Inicializa o gerenciador de janelas
        self.gerenciador_janelas = GerenciadorJanelas(self)

        # Adiciona os frames
        self.gerenciador_janelas.adicionar_frame("Login", LoginFrame)
        self.gerenciador_janelas.adicionar_frame("MenuPrincipal", MenuPrincipalFrame)

        # Mostra a tela de login inicialmente
        self.gerenciador_janelas.mostrar_frame("Login")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()