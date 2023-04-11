import domain.favorites.repository as Repository
from util.handle_response import response_error, response_ok

def add_favorite_planet(user_id,planet_id):
    return Repository.add_favorite_planet(user_id,planet_id)

  
   

def add_favorite_people():
    return

def delete_favorite_planet():
    return

def delete_favorite_people():
    return  