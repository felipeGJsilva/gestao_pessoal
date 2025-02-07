import mysql.connector
from mysql.connector import Error

class GerenciadorBancoDados:
    def __init__(self, host, usuario, senha, banco):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.senha,
                database=self.banco
            )
            return self.conexao
        except Error as e:
            print(f"Erro ao conectar ao banco: {e}")
            return None

    def executar_consulta(self, query, params=None):
        try:
            cursor = self.conexao.cursor(dictionary=True)
            cursor.execute(query, params or ())
            return cursor.fetchall()
        except Error as e:
            print(f"Erro na consulta: {e}")
            return []

    def executar_comando(self, query, params=None):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query, params or ())
            self.conexao.commit()
            return True
        except Error as e:
            print(f"Erro no comando: {e}")
            return False

    def iniciar_transacao(self):
        self.conexao.start_transaction()

    def confirmar_transacao(self):
        self.conexao.commit()

    def reverter_transacao(self):
        self.conexao.rollback()