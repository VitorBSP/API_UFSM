from extensions import db

list_alunos = []

def get_last_id():
    if list_alunos:
        last_aluno = list_alunos[-1]
    else:
        return 1
    return last_aluno.id + 1


class Cursos(db.Model):
    __tablename__ = 'cursos'
    
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(200))
    num_of_graduated = db.Column(db.Integer)
    rate = db.Column(db.Integer)
    city_country = db.Column(db.String(1000))
    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, 
                            server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, 
                            server_default=db.func.now(), onupdate=db.func.now())
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))