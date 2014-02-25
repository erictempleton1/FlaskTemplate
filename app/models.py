from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), index = True)
    email = db.Column(db.String(), index = True, unique = True)
    nickname = db.Column(db.String(), index = True, unique = True)
    location = db.relationship('UserLocation', backref = 'user', 
                                lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % (self.name)


class UserLocation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    city = db.Column(db.String())
    state = db.Column(db.String(2))
    country = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<UserLocation %r>' % (self.city)