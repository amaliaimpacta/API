from flask import Flask, jsonify

# Cria a aplicação Flask
app = Flask(__name__)

# Cria uma rota para a consulta de informações
@app.route('/', methods=['GET'])
def consulta():
    # Simula informações sendo buscadas do banco de dados
    informacoes = {'nome': 'Amalia', 'faculdade': 'Impacta', 'matricula': '2200519', 'AC': '02', 'turma': 'ADS3B'}

    # Retorna as informações em formato JSON
    return jsonify(informacoes)

if __name__ == '__main__':
    app.run()
