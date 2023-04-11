from models.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    favorites = db.relationship('Favorites',back_populates='user')
  
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
      
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

    def serialize_favorites(self):
        return {
            "id":self.id,
            "username":self.username,
            "email": self.email,
            "favorites": list(map(lambda favorite: favorite.serialize_fav_user(),self.favorites))
        }