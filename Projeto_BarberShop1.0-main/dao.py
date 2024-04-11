# dao.py
import mysql.connector

class UsuarioDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "",
            database = "Login"
        )

    def __del__(self):
        self.conexao.close()

    def inserir_usuario(self, email, senha):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Usuários (email, senha) VALUES (%s, %s)", (email, senha))
        self.conexao.commit()
        cursor.close()

    def validar_credenciais(self, email, senha):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Usuários WHERE email = %s AND senha = %s", (email, senha))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado is not None
    
    
class agendamentoDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "",
            database = "Login"
        )

    def __del__(self):
        self.conexao.close()

    def inserir_agendamento(self, Nome, Dia, horário, Barbeiro, Tipo_corte):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Agendamento (Nome, Dia, horário, Barbeiro, Tipo_corte) VALUES (%s, %s, %s, %s, %s)", (Nome, Dia, horário, Barbeiro, Tipo_corte))
        self.conexao.commit()
        cursor.close()


