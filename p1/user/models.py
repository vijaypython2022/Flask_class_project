from p1 import db

from flask import jsonify
class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    dob=db.Column(db.Date)

    def __repr__(self):
        #return "<User %r>" % {self.username}
        #
        #
        return {
            'username':self.username,
            'email':self.email,
            'password':self.password,
            'dob':self.dob
        }

    # User('abc',"xyz",30)
