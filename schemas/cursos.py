from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError
from schemas.user import UserSchema


def validate_rate(n):
        if n < 0:
            raise ValidationError('Number of servings must be greater than 0.')
        if n > 10:
            raise ValidationError('Number of servings must not be greater than 10.')

class CursosSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(dump_only=True)
    course = fields.String(required=True, validate=[validate.Length(max=100)])
    comment = fields.String(required=True, validate=[validate.Length(max=1000)])
    num_of_graduated = fields.Integer(required=True)
    rate = fields.Integer(required=True, validate = validate_rate)
    city_country = fields.String(validate=[validate.Length(max=150)])
    is_publish = fields.Boolean(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    author = fields.Nested(UserSchema, attribute='user', dump_only=True, only=['id', 'username'])
    
    @validates('num_of_graduated')
    def validate_num_of_graduated(self, value):
        if value < 0:
            raise ValidationError('Number of graduated must be equal or greather than 0')
    
    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}
        return data
