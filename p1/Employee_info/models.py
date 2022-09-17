from p1 import db

from flask import jsonify

# create association table
emp_association = db.Table("emp_association",
                           db.Column("emp_id", db.Integer, db.ForeignKey("emp.emp_id"), primary_key=True),
                           db.Column("address_id", db.Integer, db.ForeignKey("emp_address.id"),primary_key=True))


class Employee(db.Model):
    __tablename__ = 'emp'
    id = db.Column("emp_id", db.Integer, primary_key=True, autoincrement=True)
    username = db.Column("emp_name", db.String(30), nullable=False)
    email = db.Column("emp_email", db.String(100), nullable=False)
    password = db.Column("pwd", db.String(150), nullable=False)
    emp_age = db.relationship("Emp_age", backref="emp", lazy=True, uselist=False, cascade='all,delete')
    addresses = db.relationship("Emp_address", secondary=emp_association, backref="emp", lazy="joined",
                                cascade="all,delete")

    def to_representation(self):
        if self.emp_age:
            emp_age = self.emp_age.to_representation()
        else:
            emp_age = {}
        if self.addresses:
            addresses=[x.to_representation() for x in self.addresses]
        else:
            addresses=[]
        return {
            'id':self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'age': emp_age,
            'city':addresses
        }


class Emp_age(db.Model):
    __tablename__ = 'emp_age'
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    age = db.Column("age", db.Integer, nullable=True)
    emp_id = db.Column("emp_id", db.Integer, db.ForeignKey('emp.emp_id'), nullable=False)

    def to_representation(self):
        return {
            'age': self.age,
        }


class Emp_address(db.Model):
    __tablename__ = 'emp_address'
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    city = db.Column("city", db.String(25), nullable=True)

    def to_representation(self):
        return {
            'city': self.city,
        }
