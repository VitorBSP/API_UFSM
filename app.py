from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db

from resources.user import UserListResource
from resources.aluno import AlunoListResource, AlunoResource, AlunoPublishResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)

def register_resources(app):
    api = Api(app)
    api.add_resource(UserListResource, '/users')
    api.add_resource(AlunoListResource, '/alunos')
    api.add_resource(AlunoResource, '/alunos/<int:aluno_id>')
    api.add_resource(AlunoPublishResource, '/alunos/<int:aluno_id>/publish')

# @app.route("/")
# def hello():

#     return "Hello World!"

if __name__ == '__main__':
    app = create_app()
    app.run()


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