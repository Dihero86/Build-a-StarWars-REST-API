import domain.user.repository as Repository
from util.handle_response import response_error, response_ok

def create_user(body):
    if body['username'] is None or body['username']=='':
        return response_error('Username not valid', 400)
    if body['email'] is None or body['email']=='':
        return response_error('email not valid', 400)   
    return response_ok(Repository.create_user(body),201)

def get_all_user():
    return response_ok(Repository.get_all_user(),200)

def get_one_user(id):
    user= Repository.get_one_user(id)
    print(user)
    if user is None:
        return response_error("user not found", 404)
    return response_ok(user, 200)

