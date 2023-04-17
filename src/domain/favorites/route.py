from flask import Flask,request
import domain.favorites.controller as Controller

def favorites_route(app):

    @app.route('/favorite/planet/<int:planet_id>',methods=['POST'])
    def add_favorite_planet (planet_id):
        user_id = request.get_json()['user_id']
        favorite= Controller.add_favorite_planet(user_id, planet_id)
        
        return 
    
    @app.route('/favorite/people/<int:people_id>',methods=['POST'])
    def add_favorite_people (people_id):
        user_id = request.get_json()['user_id']
        new_favorite=Favorites(user_id, None, people_id)
        db.session.add(new_favorite)
        db.session.commit()
        return new_favorite.serialize_fav()

    @app.route('/favorite/planet/<int:planet_id>',methods=['DELETE'])
    def delete_favorite_planet (planet_id):
        user = request.get_json()['user_id']
        delete_favorite = Favorites.query.filter_by(user_id=user, planet_id=planet_id).first()
        db.session.delete(delete_favorite)
        db.session.commit()
        return 'hola'

    @app.route('/favorite/people/<int:people_id>',methods=['DELETE'])
    def delete_favorite_people (people_id):
        data = request.get_json()['user_id']
        delete_favorite = Favorites.query.filter_by(user_id=data, people_id=people_id).first()
        db.session.delete(delete_favorite)
        db.session.commit()
        return 'hola'