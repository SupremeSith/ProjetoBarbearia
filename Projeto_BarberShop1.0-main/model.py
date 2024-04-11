import mysql.connector
from app import *

# classe com funções para retornar (get) o usuário
class RetornoUser:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "",
            database = "Login"
        )

    def __del__(self):
        self.conexao.close()

    def get_usuario(self, email):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Usuários WHERE email = %s", (email))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado
    
    def get_agendamento(self, Nome, Dia, horário, Barbeiro, Tipo_corte):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Agendamento WHERE Nome = %s AND Dia = %s AND horário = %s AND Barbeiro = %s AND Tipo_corte = %s", (Nome, Dia, horário, Barbeiro, Tipo_corte))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado

