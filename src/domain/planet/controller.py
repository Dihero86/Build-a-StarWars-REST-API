import domain.planet.repository as Repository
from util.handle_response import response_error, response_ok

def add_planet(body):
    if body['name_planet'] is None or body['name_planet']=='':
        return response_error("name planet not valid",400)
    return response_ok(Repository.add_planet(body),201)

def get_all_planets():
    return response_ok(Repository.get_all_planets(),200)

def get_planet(id):
    planeta= Repository.get_planet(id)
    if planeta is None:
        return response_error('planet not found',404) 
    return response_ok(planeta,200)