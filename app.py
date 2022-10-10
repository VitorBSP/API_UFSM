
from flask import Flask, jsonify, request
from http import HTTPStatus
from flask_restful import Api
from resources.aluno import AlunoListResource, AlunoResource, AlunoPublishResource

alunos =    [
                {
                    'id' : 1,
                    'curso' : 'Estatística',
                    'anoIngresso' : 2018,
                    'anoEvasao' : 2023,
                    'tipoEvasao' : 1
                },

                {
                    'id' : 2,
                    'curso' : 'Oceanografia',
                    'anoIngresso' : 2022,
                    'anoEvasao' : 2027,
                    'tipoEvasao' : 1
                }
            ]

app = Flask(__name__)
api = Api(app)

api.add_resource(AlunoListResource, '/alunos')
api.add_resource(AlunoResource, '/alunos/<int:aluno_id>')
api.add_resource(AlunoPublishResource, '/alunos/<int:aluno_id>/publish')

@app.route("/")
def hello():

    return "Hello World!"


# @app.route('/alunos', methods=['GET'])
# def get_alunos():
#     return jsonify({'data' : alunos})

# @app.route('/alunos/<int:aluno_id>', methods=['GET'])
# def get_aluno(aluno_id):
#     aluno = next((aluno for aluno in alunos if aluno['id'] == aluno_id), None)
#     if aluno:
#         return jsonify(aluno)
#     return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

# @app.route('/alunos', methods = ['POST'])
# def create_alunos():
#         data = request.get_json()
#         curso = data.get('curso')
#         anoIngresso = data.get('anoIngresso')
#         anoEvasao = data.get('anoEvasao')
#         tipoEvasao = data.get('tipoEvasao')
#         aluno = {
#                     'id' : len(alunos) + 1,
#                     'curso' : curso,
#                     'anoIngresso' : anoIngresso,
#                     'anoEvasao' : anoEvasao,
#                     'tipoEvasao' : tipoEvasao
#                 }
#         alunos.append(aluno)
#         return jsonify(aluno), HTTPStatus.CREATED

# @app.route('/alunos/<int:aluno_id>', methods = ['PUT'])
# def update_alunos(aluno_id):
#     aluno = next((aluno for aluno in alunos if aluno['id'] == aluno_id), None)
#     if not aluno:
#         return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
#     data = request.get_json()
#     aluno.update({
#                     'curso' : data.get('curso'),
#                     'anoIngresso' : data.get('anoIngresso'),
#                     'anoEvasao' : data.get('anoEvasao'),
#                     'tipoEvasao' : data.get('tipoEvasao')
#                     })
#     return jsonify(aluno)
    
# @app.route('/alunos/<int:aluno_id>', methods = ['DELETE'])
# def delete_aluno(aluno_id):
#     aluno = next((aluno for aluno in alunos if aluno['id'] == aluno_id), None)
#     if not aluno:
#         return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
#     alunos[:] = [aluno for aluno in alunos if aluno.get('id') != aluno_id]
#     return jsonify(alunos)

if __name__ == "__main__":

    app.run(port= 5000, debug=True)