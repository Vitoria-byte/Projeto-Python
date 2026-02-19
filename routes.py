from flask import Blueprint, jsonify, request, render_template
from flask_cors import CORS
from app.database import get_conexao

routes = Blueprint('routes', __name__)
CORS(routes)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/api/produtos', methods=['GET'])
def listar():
    conexao = get_conexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute('SELECT * FROM produtos')
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(dados)

@routes.route('/api/produtos', methods=['POST'])
def cadastrar():
    dados = request.json
    conexao = get_conexao()
    cursor = conexao.cursor()
    sql = 'INSERT INTO produtos (nome, quantidade, preco) VALUES (%s, %s, %s)'
    cursor.execute(sql, (dados['nome'], dados['quantidade'], dados['preco']))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({'mensagem': 'Produto cadastrado'})

@routes.route('/api/produtos/<int:id>', methods=['PUT'])
def editar(id):
    dados = request.json
    conexao = get_conexao()
    cursor = conexao.cursor()
    sql = 'UPDATE produtos SET nome=%s, quantidade=%s, preco=%s WHERE id=%s'
    cursor.execute(sql, (dados['nome'], dados['quantidade'], dados['preco'], id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return jsonify({'mensagem': 'Produto atualizado'})

@routes.route('/api/produtos/<int:id>', methods=['DELETE'])
def deletar(id):
    return jsonify({'erro': 'Delete não permitido'}), 403
