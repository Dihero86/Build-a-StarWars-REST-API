import domain.favorites.repository as Repository
from util.handle_response import response_error, response_ok
from domain.user.repository import get_one_user
from domain.planet.repository import get_planet
from domain.people.repository import get_one_people

def add_favorite_planet(user_id,planet_id):
    user=get_one_user(user_id)
    planet=get_planet(planet_id)
    if user is None or planet is None:
        return response_error('not Found', 404) 
    return response_ok(Repository.add_favorite_planet(user_id, planet_id), 201)

def add_favorite_people(user_id,people_id):
    user=get_one_user(user_id)
    people=get_one_people(people_id)
    if user is None or people is None:
        return response_error('not Found', 404) 
    return response_ok(Repository.add_favorite_people(user_id, people_id), 201)

def delete_favorite_planet(user_id,planet_id):
    favorito= Repository.delete_favorite_planet(user_id, planet_id)
    if favorito is None:
        return response_error('favorite not Found, nothing to delete', 404) 
    return response_ok(favorito, 200)

def delete_favorite_people(user_id,people_id):
    favorito= Repository.delete_favorite_people(user_id, people_id)
    if favorito is None:
        return response_error('favorite not Found, nothing to delete', 404) 
    return response_ok(favorito, 200)


def get_favorites_user(id):
    user_favorites = Repository.get_favorites_user(id)
    if not user_favorites:
        return response_error('user has not favorites', 200)
    return response_ok(user_favorites, 200)

    