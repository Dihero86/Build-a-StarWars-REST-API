from models.db import db

class Favorites(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id= db.Column(db.Integer, db.ForeignKey('planet.id'))
    people_id= db.Column(db.Integer, db.ForeignKey('people.id'))
    user= db.relationship('User',back_populates='favorites')
    planet= db.relationship('Planet', back_populates='favorites')
    people= db.relationship('People')

    def __init__(self,user_id,planet_id,people_id):
        self.user_id = user_id
        self.planet_id = planet_id
        self.people_id = people_id

    def __repr__(self):
        return '<Favorites %r>' % self.user_id

    def serialize_favorites_planets(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user":self.user.serialize(),
            "planet_id": self.planet_id,
            "planet": self.planet.serialize(),  
        }

    def serialize_favorites_people(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user":self.user.serialize(),
            "people_id": self.people_id,
            "people": self.people.serialize(),  
        }
