from gerenciador_banco import GerenciadorBancoDados

class FuncionarioController:
    def __init__(self):
        self.db = GerenciadorBancoDados(host="localhost", usuario="root", senha="", banco="gestao_pessoal")
        self.db.conectar()

    def cadastrar_funcionario(self, nome, cpf, cargo, departamento, email, data_contratacao):
        query = """
        INSERT INTO Funcionarios (nome, cpf, cargo, departamento, email, data_contratacao)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (nome, cpf, cargo, departamento, email, data_contratacao)
        return self.db.executar_comando(query, valores)

    def listar_funcionarios(self):
        query = "SELECT * FROM Funcionarios"
        return self.db.executar_consulta(query)