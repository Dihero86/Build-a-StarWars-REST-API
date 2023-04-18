from flask import Flask,request
import domain.user.controller as Controller

def user_route(app):

    @app.route('/users',methods=['POST'])
    def create_user():
        data = request.get_json()
        return Controller.create_user(data)

    @app.route('/users', methods=['GET'])
    def get_all_user():
        return Controller.get_all_user()

    @app.route('/users/<int:id>', methods=['GET'])
    def get_one_user(id):
        return Controller.get_one_user(id)

  
