from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.cursos import Cursos  
from flask_jwt_extended import (jwt_required, get_jwt_identity)

class AlunoListResource(Resource):
    def get(self):

        cursos = Cursos.get_all_published()
        data = []
        
        for curso in cursos:
            data.append(curso.data())
        
        return {'data' : data}, HTTPStatus.OK
    
    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user = get_jwt_identity()

        curso = Cursos(
                        course = data['curso'],
                        comment = data['comment'],
                        num_of_graduated = data['num_of_graduated'],
                        rate = data['rate'],
                        city_country = data['city'],
                        user_id = current_user
                    )
        
        curso.save()
            
        return curso.data(), HTTPStatus.CREATED


class AlunoResource(Resource):
    
    @jwt_required(optional=True)
    def get(self, curso_id):

        curso = Cursos.get_by_id(curso_id)

        if curso is None:
            return {'message' : 'studant not found'}, HTTPStatus.NOT_FOUND
        
        current_user = get_jwt_identity()

        if curso.is_publish == False and curso.user_id != current_user:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        data = curso.data()

        return data, HTTPStatus.OK
  
    @jwt_required()
    def put(self, curso_id):

        data = request.get_json()

        curso = Cursos.get_by_id(curso_id)

        if curso is None:
            return {'message' : 'studant not found'}, HTTPStatus.NOT_FOUND
        
        current_user = get_jwt_identity()

        if current_user != curso.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN
        
        curso.course = data['curso']
        curso.comment = data['comment']
        curso.num_of_graduated = data['num_of_graduated']
        curso.rate = data['rate']
        curso.city_country = data['city']
        curso.save()

        return curso.data(), HTTPStatus.OK

    @jwt_required()
    def delete(self, curso_id):

        curso = Cursos.get_by_id(curso_id)

        if curso is None:
            return {'message' : 'studant not found'}, HTTPStatus.NOT_FOUND
        
        current_user = get_jwt_identity()

        if current_user != curso.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN
        
        curso.delete()

        return {}, HTTPStatus.NO_CONTENT


class AlunoPublishResource(Resource):
    # Os métodos put e delete estão sendo usados de maneira flexível, 
    # não necessariamente para atualizar ou deletar o conteúdo 
    @jwt_required()
    def put(self, curso_id):

        curso = Cursos.get_by_id(curso_id)

        if curso is None:
            return {'message' : 'studant not found'}, HTTPStatus.NOT_FOUND
        
        current_user = get_jwt_identity()

        if current_user != curso.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        curso.is_publish = True
        curso.save()

        return {}, HTTPStatus.NO_CONTENT

    @jwt_required()
    def delete(self, curso_id):
        curso = Cursos.get_by_id(curso_id)

        if curso is None:
            return {'message' : 'studant not found'}, HTTPStatus.NOT_FOUND
        
        current_user = get_jwt_identity()

        if current_user != curso.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        curso.is_publish = False
        curso.save()

        return {}, HTTPStatus.NO_CONTENT