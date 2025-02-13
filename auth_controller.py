from gerenciador_banco import GerenciadorBancoDados

class AuthController:
    def __init__(self):
        self.db = GerenciadorBancoDados(host="localhost", usuario="root", senha="", banco="gestao_pessoal")
        self.db.conectar()

    def autenticar(self, usuario, senha):
        query = "SELECT * FROM Usuarios WHERE usuario = %s AND senha = %s"
        valores = (usuario, senha)
        resultado = self.db.executar_consulta(query, valores)
        return resultado[0] if resultado else None