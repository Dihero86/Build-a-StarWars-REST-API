from models.index import db, User

def create_user(body):
    new_user= User(body['username'],body['email'],body['password'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def get_all_user():
    all_users= User.query.all()
    serialize_user= list(map(lambda user: user.serialize(),all_users))
    return serialize_user

def get_favorites_user(id):
    user= User.query.get(id)
    if user is None:
        return user
    return user.serialize_favorites()