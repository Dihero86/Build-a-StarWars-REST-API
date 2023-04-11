from models.db import db

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_character = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(120), unique=False, nullable=False)
    mass = db.Column(db.String(120), unique=False, nullable=False)
    
    def __init__(self,name_character,height,mass):
        self.name_character = name_character
        self.height = height
        self.mass = mass
      
    def __repr__(self):
        return '<People %r>' % self.name_character

    def serialize(self):
        return {
            "id": self.id,
            "name_character": self.name_character,
            "height": self.height,
            "mass": self.mass
        }