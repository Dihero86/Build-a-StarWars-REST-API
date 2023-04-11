from flask import Flask, request
import domain.people.controller as Controller

def people_route(app):

    @app.route('/people', methods=['GET'])
    def get_all_people():
        return Controller.get_all_people()

    @app.route('/people', methods=['POST'])
    def addpeople():
        data = request.get_json()
        return Controller.addpeople(data)

    @app.route('/people/<int:id>', methods=['GET'])
    def get_one_people(id):
        return Controller.get_one_people(id)
       