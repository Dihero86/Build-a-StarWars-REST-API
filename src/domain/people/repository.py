from models.index import db,People

def addpeople(data):
    new_people = People(data['name_character'], data['height'], data['mass'])
    db.session.add(new_people)
    db.session.commit()
    return new_people.serialize()

def get_all_people():
    all_people = People.query.all()
    serialize_people = list(map(lambda people: people.serialize(),all_people))
    return serialize_people

def get_one_people(id):
    people= People.query.get(id)
    if people is None:
        return people
    return people.serialize()