from flask import Flask, request
from models.index import db, Favorites

def add_favorite_planet(user_id,planet_id):
    new_favorite=Favorites(user_id, planet_id, None)
    db.session.add(new_favorite)
    db.session.commit()
    return new_favorite.serialize_fav()

def add_favorite_people():
    return

def delete_favorite_planet():
    return

def delete_favorite_people():
    return  