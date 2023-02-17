from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.aluno import Aluno, list_alunos


class AlunoListResource(Resource):
    def get(self):
        data = []
        for aluno in list_alunos:
            if aluno.is_publish is True:
                data.append(aluno.data)
        return {'data' : data}, HTTPStatus.OK
    
    def post(self):
        data = request.get_json()
        aluno = Aluno  (
                            curso = data['curso'],
                            anoIngresso = data['anoIngresso'],
                            anoEvasao = data['anoEvasao'],
                            tipoEvasao = data['tipoEvasao']
                        )
        list_alunos.append(aluno)
            
        return aluno.data, HTTPStatus.CREATED


class AlunoResource(Resource):
    def get(self, aluno_id):
        aluno = (next((aluno for aluno in list_alunos 
                        if aluno.id == aluno_id and aluno.is_publish == True), 
                        None))
        if aluno is None:
            return {'message' : 'studant not found'}, HTTPStatus.NOT_FOUND
        return aluno.data, HTTPStatus.OK

    def put(self, aluno_id):
        data = request.get_json
        aluno = (next((aluno for aluno in list_alunos 
                        if aluno.id == aluno_id), None))
        if aluno is None:
            return {'message' : 'studant not found'}, HTTPStatus.NOT_FOUND

        aluno.curso = data['curso']
        aluno.anoIngressso = data['anoIngresso'],
        aluno.anoEvasao = data['anoEvasao'],
        aluno.tipoEvasao = data['tipoEvasao']

        return aluno.data, HTTPStatus.OK

class AlunoPublishResource(Resource):
    # Os métodos put e delete estão sendo usados de maneira flexível, 
    # não necessariamente para atualizar ou deletar o conteúdo 
    def put(self, aluno_id):
        aluno = (next((aluno for aluno in list_alunos 
                        if aluno.id == aluno_id), None))
        if aluno is None:
            return {'message' : 'studant not found'}, HTTPStatus.NOT_FOUND

        aluno.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, aluno_id):
        aluno = (next((aluno for aluno in list_alunos 
                        if aluno.id == aluno_id), None))
        if aluno is None:
            return {'message' : 'studant not found'}, HTTPStatus.NOT_FOUND

        aluno.is_publish = False

        return {}, HTTPStatus.NO_CONTENT