from p1 import db

from flask import jsonify
class Employee(db.Model):
    __tablename__='emp'
    id=db.Column("emp_id",db.Integer,primary_key=True)
    username = db.Column("emp_name",db.String(30), nullable=False)
    email = db.Column("emp_email",db.String(100), nullable=False)
    password = db.Column("pwd",db.String(150), nullable=False)
    emp_age=db.relationship("Emp_age",backref="user",lazy=True,uselist=False,cascade='all,delete')


    def to_representation(self):
        if self.emp_age:
            emp_age=self.email.to_representation()
        else:
            emp_age={}

        return {
            'username':self.username,
            'email':self.email,
            'password':self.password,
            'age':emp_age
        }

class Emp_age(db.Model):
    __tablename__='emp_age'
    id = db.Column("id", db.Integer, primary_key=True,autoincrement=True)
    age = db.Column("age", db.Integer, nullable=True)
    emp_id=db.Column("emp_id",db.Integer,db.ForeignKey('emp.emp_id'),nullable=False)

    def to_representation(self):
        return{
            'age':self.age,
        }