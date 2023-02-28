from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db, jwt

from resources.token import TokenResource, RefreshResource, RevokeResource, black_list
from resources.user import UserListResource, UserResource, UserTesting, MeResource
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
    jwt.init_app(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        return jti in black_list
    
def register_resources(app):
    api = Api(app)
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<string:username>')
    api.add_resource(UserTesting, '/users/<int:user_id>')
    api.add_resource(MeResource, '/me') 

    api.add_resource(AlunoListResource, '/alunos')
    api.add_resource(AlunoResource, '/alunos/<int:curso_id>')
    api.add_resource(AlunoPublishResource, '/alunos/<int:curso_id>/publish')

    api.add_resource(TokenResource, '/token')
    api.add_resource(RefreshResource, '/refresh')
    api.add_resource(RevokeResource, '/revoke') 
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