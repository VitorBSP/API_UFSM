from flask import request
from flask_restful import Resource
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from http import HTTPStatus
from utils import hash_password

from models.user import User
from extensions import db
from schemas.user import UserSchema

user_schema = UserSchema()
user_public_schema = UserSchema(exclude=('email',))

class UserListResource(Resource):
    def post(self):
        
        json_data = request.get_json()

        data, errors = user_schema.load(data=json_data)

        if errors:
            return {'message': 'Validation errors', 'errors': errors}, HTTPStatus.BAD_REQUEST

        if User.get_by_username(data.get('username')):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST

        if User.get_by_email(data.get('email')):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST

        password = hash_password(data.get('password'))

        user = User(**data)
        user.save()

        return user_schema.dump(user), HTTPStatus.CREATED
    
class UserTesting(Resource):
    def get(self, user_id):
        user = User.get_by_id(user_id)
        return {'id' : user.id, 
                'username' : user.username,
                'email' : user.email}, HTTPStatus.OK

class UserResource(Resource):
    @jwt_required(optional=True)
    def get(self, username):
        
        user = User.get_by_username(username=username)
        
        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
        
        current_user = get_jwt_identity()

        if current_user == user.id:
            data = user_schema.dump(user)
        else:
            data = user_public_schema.dump(user)
        
        return data, HTTPStatus.OK

class MeResource(Resource):
    @jwt_required()
    def get(self):
        user = User.get_by_id(id=get_jwt_identity())
        return user_schema.dump(user), HTTPStatus.OK
