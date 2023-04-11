import domain.people.repository as Repository
from util.handle_response import response_error, response_ok

def addpeople(data):
    if data['name_character'] is None or data['name_character'] == '':
        return ( 'Name not valid', 400)
    return response_ok(Repository.addpeople(data), 201)

def get_all_people():
    return response_ok(Repository.get_all_people(), 200)

def get_one_people(id):
    people= Repository.get_one_people(id)
    if people is None:
        return response_error('Character not found', 404)
    return response_ok(people, 200)
