from flask import request
from flask_restful import Resource
from http import HTTPStatus
from pprint import pprint
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from marshmallow import ValidationError

from models.cursos import Cursos  
from schemas.cursos import CursosSchema

cursos_schema = CursosSchema()
cursos_list_schema = CursosSchema(many=True)

class AlunoListResource(Resource):
    def get(self):

        cursos = Cursos.get_all_published()

        return cursos_list_schema.dump(cursos), HTTPStatus.OK
    
    @jwt_required()
    def post(self):
        json_data = request.get_json()
        current_user = get_jwt_identity()

        try:
            data = cursos_schema.load(json_data)
        except ValidationError as err:
            pprint(err.messages)

        curso = Cursos(**data)
        curso.user_id = current_user        
        curso.save()
            
        return cursos_schema.dump(curso), HTTPStatus.CREATED


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
    
    @jwt_required()
    def patch(self, curso_id):
            print('------------------------')
            json_data = request.get_json()

            
            data = cursos_schema.load(json_data)
            
            curso = Cursos.get_by_id(curso_id)

            print(curso.course)
            print('try')
            print(data)
            print(data['comment'])

            if curso is None:
                return {'message': 'Course not found'}, HTTPStatus.NOT_FOUND
            
            current_user = get_jwt_identity()
            if current_user != curso.user_id:
                return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN
            
            curso.course = data.get('course') or curso.course
            curso.comment = data.get('comment') or curso.comment
            curso.num_of_graduated = data.get('num_of_graduated')  or curso.num_of_graduated
            curso.rate = data.get('rate')  or curso.rate
            curso.city_country = data.get('city_country') or curso.city_country
            curso.save()

            return cursos_schema.dump(curso), HTTPStatus.OK


class AlunoPublishResource(Resource):
    # Os métodos put e delete estão sendo usados de maneira flexível, 
    # não necessariamente para atualizar ou deletar o conteúdo 
    @jwt_required()
    def put(self, curso_id):
        print('---')

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