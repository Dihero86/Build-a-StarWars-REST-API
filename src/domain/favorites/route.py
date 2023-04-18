from flask import Flask,request
import domain.favorites.controller as Controller

def favorites_route(app):

    @app.route('/favorite/planet/<int:planet_id>',methods=['POST'])
    def add_favorite_planet (planet_id):
        user_id = request.get_json()['user_id']
        return Controller.add_favorite_planet(user_id, planet_id) 
    
    @app.route('/favorite/people/<int:people_id>',methods=['POST'])
    def add_favorite_people (people_id):
        user_id = request.get_json()['user_id']
        return Controller.add_favorite_people(user_id, people_id)

    @app.route('/favorite/planet/<int:planet_id>',methods=['DELETE'])
    def delete_favorite_planet (planet_id):
        user_id = request.get_json()['user_id']
        return Controller.delete_favorite_planet(user_id,planet_id)

    @app.route('/favorite/people/<int:people_id>',methods=['DELETE'])
    def delete_favorite_people (people_id):
        user_id = request.get_json()['user_id']
        return Controller.delete_favorite_people(user_id, people_id)

    @app.route('/users/favorites/<int:id>',methods=['GET'])
    def get_favorites_user(id):
        return Controller.get_favorites_user(id)