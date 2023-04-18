from flask import Flask, request
from models.index import db, Favorites

def add_favorite_planet(user_id,planet_id):
    new_favorite=Favorites(user_id, planet_id, None)
    db.session.add(new_favorite)
    db.session.commit()
    return new_favorite.serialize_favorites_planets()

def add_favorite_people(user_id,people_id):
    new_favorite=Favorites(user_id, None, people_id)
    db.session.add(new_favorite)
    db.session.commit()
    return new_favorite.serialize_favorites_people()

def delete_favorite_planet(user_id,planet_id):
    delete_favorite = Favorites.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if delete_favorite is None:
        return delete_favorite
    db.session.delete(delete_favorite)
    db.session.commit()
    return get_favorites_user(user_id)

def delete_favorite_people(user_id,people_id):
    delete_favorite = Favorites.query.filter_by(user_id=user_id, people_id=people_id).first()
    if delete_favorite is None:
        return delete_favorite
    db.session.delete(delete_favorite)
    db.session.commit()
    return ({"msg":"personaje borrado"})

def get_favorites_user(id):
    favoritos= Favorites.query.filter_by(user_id=id).all()
    if favoritos is None:
        return favoritos
    serializados=[]
    for elemento in favoritos:
        if elemento.people_id is None:
            serializados.append(elemento.serialize_favorites_planets())
        else:
            serializados.append(elemento.serialize_favorites_people())
    return serializados