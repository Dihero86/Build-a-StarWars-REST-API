from models.db import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_planet = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.Integer, unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    favorites = db.relationship('Favorites',back_populates='planet')

    def __init__(self,name_planet,diameter,population):
        self.name_planet = name_planet
        self.diameter = diameter
        self.population = population
      
    def __repr__(self):
        return '<Planet %r>' % self.name_planet

    def serialize(self):
        return {
            "id": self.id,
            "name_planet": self.name_planet,
            "diameter": self.diameter,
            "population": self.population
        }

    def serialize_planet(self):
        return {
            "name_planet": self.name_planet
        }