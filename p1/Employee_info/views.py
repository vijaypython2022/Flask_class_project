from flask import Blueprint,request,jsonify
from p1.Employee_info.models import Employee,Emp_age,Emp_address
from p1 import db

mod=Blueprint('emp',__name__)

@mod.route('/insert_emp',methods=['POST'])
def create_emp():
    emp_data=request.get_json()
    emp=Employee(
        username=emp_data['username'],
        email=emp_data['email'],
        password=emp_data['password']
    )
    db.session.add(emp)
    db.session.commit()
    return jsonify({'status':'User added'})

@mod.route('/get_emp',methods=['GET'])
def get_emp():
    emp_data=Employee.query.all()
    emp=[x.to_representation() for x in emp_data]
    return jsonify(emp)

@mod.route('/insert_age',methods=['POST'])
def insert_emp_age():
    emp_data=request.get_json()
    age=Emp_age(
        age=emp_data['age'],
        emp_id=emp_data['emp_id']
        )
    db.session.add(age)
    db.session.commit()
    return jsonify({'status':'age added'})


@mod.route('/insert_city',methods=['POST'])
def insert_city():
    emp_data=request.get_json()
    emp_id=emp_data['emp_id']
    address=Emp_address(city=emp_data['city'])
    data=Employee.query.get(emp_id)
    data.addresses.append(address)

    db.session.commit()
    return jsonify({'status':'Address added'})












