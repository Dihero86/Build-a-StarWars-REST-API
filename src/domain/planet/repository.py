from models.index import db,Planet

def add_planet(body):
    new_planet=Planet(body['name_planet'],body['diameter'],body['population'])
    db.session.add(new_planet)
    db.session.commit()
    return new_planet.serialize()

def get_all_planets():
   all_planets= Planet.query.all()
   serialize_planet= list(map(lambda planet: planet.serialize(), all_planets))
   return serialize_planet

def get_planet(id):
    planet= Planet.query.get(id)
    if planet is None:
        return planet
    return planet.serialize()