from extensions import db


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

    def data(self):
        return {
                'id': self.id,
                'course': self.course,
                'comment': self.comment,
                'num_of_graduated': self.num_of_graduated,
                'rate': self.rate,
                'city_country': self.city_country,
                'user_id': self.user_id
                }
    
    @classmethod
    def get_all_published(cls):
            return cls.query.filter_by(is_publish=True).all()
    
    @classmethod
    def get_by_id(cls, curso_id):
            return cls.query.filter_by(id=curso_id).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()