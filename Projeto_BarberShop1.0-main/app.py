# app.py
from flask import Flask, render_template, jsonify, request
from dao import UsuarioDAO
from model import *

app = Flask(__name__, static_url_path='/static')
usuario_dao = UsuarioDAO()

@app.route('/')
def index():
    return render_template('cadastro.html')


@app.route('/insert', methods=['POST'])
def insert_usuario():
    dados = request.get_json()
    email = dados['email']
    senha = dados['senha']

    try:
        usuario_dao.inserir_usuario(email, senha)
        return jsonify({'message': 'Cadastro realizado com sucesso!'}), 200
    except Exception as e:
        print("Erro ao inserir dados:", e)
        return jsonify({'error': 'Ocorreu um erro ao cadastrar o usuário.'}), 500

@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    email = dados['email']
    senha = dados['senha']

    if usuario_dao.validar_credenciais(email, senha):
        return jsonify({'message': 'Login bem-sucedido!'}), 200
    else:
        return jsonify({'error': 'Credenciais inválidas. Por favor, verifique seu email e senha.'}), 401

# Rotas adicionais
@app.route('/Cadastre-se.html')
def cadastre_se():
    return render_template('cadastre-se.html')

@app.route('/agenda.html')
def agenda():
    return render_template('agenda.html')


@app.route('/valor.html')
def valor():
    return render_template('valor.html')

@app.route('/escolha.html')
def escolha():
    return render_template('escolha.html')


@app.route('/homepage.html', methods=['GET'])
def homepage():
    #Retornar usuário
    email = request.args.get('email')
    retorno_user = RetornoUser()
    return render_template('homepage.html')

@app.route('/escolha02.html')
def escolha02():
    return render_template('escolha02.html')

@app.route('/FAQ.html')
def FAQ():
    return render_template('FAQ.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/secondPage.html')
def secondPage():
    return render_template('secondPage.html')

# E assim por diante...

if __name__ == "__main__":
    app.run(debug=True)
