from flask import Flask,request,jsonify
import domain.planet.controller as Controller

def planet_route(app):

    @app.route('/planets',methods=['POST'])
    def add_planet():
        data = request.get_json()
        return Controller.add_planet(data)

    @app.route('/planets', methods=['GET'])
    def get_all_planets():
        return Controller.get_all_planets()

    @app.route('/planets/<int:id>', methods=['GET'])
    def get_planet(id):
        return Controller.get_planet(id)
