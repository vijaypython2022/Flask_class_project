import json
from flask import Blueprint, jsonify, request, render_template, abort, redirect, url_for
from p1.user.models import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Blueprint('user', __name__)


# @app.before_first_request
# def create_table():
#     db.create_all()


# CURD Operation on Mysql db

# read data from table


@app.route('/get_all', methods=['GET'])
def fetch_user():
    # method1
    # users = User.query.all()  # select * from emp
    # res = [x.__repr__() for x in users]
    # return jsonify(res)

    # method2
    # li = []
    # for user in users:
    #     res = {
    #         "id": user.id,
    #         "username": user.username,
    #         "email": user.email,
    #         "password": user.password
    #     }
    #     li.append(res)
    #  return li

    # Method 3
    my = User.query.all()
    return render_template('view_all.html', my=my)


# get data from mysql by id

@app.route('/id/<int:id>', methods=['GET'])
def get_by_id(id):
    user_data = User.query.get(id)
    return render_template('view_all.html', user_data=user_data)


@app.route('/<int:id>', methods=['GET'])
def show_user(id):
    users = User.query.get(id)
    res = users.__repr__()
    # res.pop('password')
    return jsonify(res)


# get data from mysql by id
@app.route('/get_name', methods=['GET'])
def fetch_by_name():
    username = request.args.get('username')  # provide input ?username=vijay
    user = User.query.filter_by(username=username)  # .first()
    res = [x.__repr__() for x in user]
    # res=user.__repr__()
    # res.pop('password')
    return jsonify(res)


# write data in MYSQL table (input josn format)

@app.route('/insert', methods=['POST'])
def add_user():
    user_data = request.get_json()
    uname = user_data['username']
    email = user_data['email']
    password = user_data['password']
    data = User(username=uname, email=email, password=password)
    db.session.add(data)
    db.session.commit()
    return 'User added'


# write data in MYSQL table (input html form)
# @app.route('/get_form', methods=['GET'])
# def form_html():
#     return render_template("insert.html")


@app.route('/form_insert', methods=['GET', 'POST'])
def add_user_form():
    if request.method == 'GET':
        return render_template('insert.html')
    if request.method == 'POST':
        username = request.form.get('name')
        email = request.form.get('email')
        join = request.form.get('join_date')
        password = request.form.get('password')
        data = User(username=username, email=email, password=password, dob=join)
        db.session.add(data)
        db.session.commit()
        # return 'User added'
        return {"Status": True, "Name": username, "Email": email, "Password": password, "Dob": join}


# update table data of mysql using id
@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    id = request.get_json()
    data = User.query.get(id)
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    if data is None:
        abort(404)
    else:
        data.username = username
        data.email = email
        data.password = password
        db.session.add(data)
        db.session.commit()
        return jsonify({"Update": True, "id": id})

    # for key in user_data:
    #     if key['id']==(id):
    #         key['username']==id['username']
    #         key['email'] == id['email']
    #         key['password'] == id['password']
    # db.session.commit()
    return "User Data Updated Successfully"


@app.route('/update_form')
def update():
    return render_template('update.html')


@app.route('/update1', methods=['GET', 'POST'])
def update_user_form():
    if request.method == 'GET':
        return render_template('update.html')

    if request.method == 'POST':
        id = request.form.get('id')
        data = User.query.get(id)
        email = request.form.get('email')
        data.email = email
        db.session.commit()
        return 'updated'

    return jsonify({"Update": False})


# delete user from db using id
@app.route('/delete/<int:id>')
def delete_user(id):
    x=User.query.get(id)
    db.session.delete(x)
    db.session.commit()
    return 'user delete successfully'


# @app.route('/hello/')
@app.route('/h1')
def hello():
    name = request.args.get('name')
    return render_template('view.html', name=name)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello2(name=None):
    return render_template('view.html', name=name)


@app.route("/found/<email>")
def found(email):
    li = [1, 2, 3, 4]
    # return redirect(url_for("found", email=x, list_of_objects=y))

    return render_template("view.html", keys=email)


# *********************************************************************
# CURD operation on JSON file

# with open("p1/user/data.json") as abc:
#     data = json.load(abc)


# @app.route('/hi', methods=['GET'])
# def hellow():
#     return 'Hellow Python'


# @app.route('/', methods=['GET'])
# def fetchall():
#     return jsonify(data)

#
# @app.route('/<user_id>', methods=['GET'])
# def show_user(user_id):
#     re = [x for x in data if x['id'] == int(user_id)]
#
#     return jsonify((re))


# @app.route('/fetch_user/', methods=['GET'])
# def fetch_user():
#     show = request.args.get('user_id')
#     userdetail = [x for x in data if x['id'] == int(show)]
#     userdetail = userdetail[0] if userdetail else {}
#     return jsonify(userdetail)


# @app.route('/create', methods=['POST'])
# def create_user():
#     req_data = request.get_json()
#     name = req_data['name']
#     password = req_data['password']
#     new_id = data[-1]['id'] + 1
#     res = req_data
#     res['id'] = new_id
#     res['name'] = name
#     res['password'] = password
#     data.append(res)
#     json.dump(data, open('p1/user/data.json', 'w'))
#     return 'Data Added in file'


# @app.route('/form', methods=['POST'])
# def create_form():
#     name=request.form.get('name')
#     password = request.form.get('password')
#     new_id=data[-1]['id']+1
#     res={
#         "id": new_id,
#          "name": name,
#          "password":password
#     }
#     data.append(res)
#     json.dump(data, open('p1/user/data.json', 'w'))
#     return 'Data Added in file'

# using html form responce
# @app.route('/get_form', methods=['GET'])
# def form_html():
#     return render_template("insert.html")
#
#
# @app.route('/form_html', methods=['POST'])
# def create_form_html():
#     name = request.form.get('name')
#     password = request.form.get('password')
#     new_id = data[-1]['id'] + 1
#     res = {
#         "id": new_id,
#         "name": name,
#         "password": password
#     }
#     data.append(res)
#     json.dump(data, open('p1/user/data.json', 'w'))
#
#     return jsonify(data)


# @app.route('/update/<user_id>', methods=['PUT'])
# def update_user(user_id):
#     user_data = request.get_json()
#     for d in data:
#         if d['id'] == int(user_id):
#             if 'name' in user_data:
#                 d['name'] == user_data['name']
#             if 'password' in user_data:
#                 d['password'] == user_data['password']
#     json.dump(data, open('p1/user/data.json', 'w'))
#     return 'User Data Updated'


# @app.route('/del/<user_id>', methods=['DELETE','GET'])
# def delete_user(user_id):
#     for index, d in enumerate(data):
#         if d['id'] == int(user_id):
#             del data[index]
#     json.dump(data, open('p1/user//data.json', 'w'))
#     return jsonify(data)

@app.route('/search', methods=['GET'])
def get_form():
    return render_template('search.html')


from sqlalchemy import extract


@app.route('/month', methods=['GET'])
def get_by_month():
    input_month = request.args.get('month')
    mydata = User.query.filter(extract('month', User.dob) == input_month).all()

    res = [x.__repr__() for x in mydata]

    return res

# provide two value get all record using or
from sqlalchemy import or_
@app.route('/get_by_or',methods=['GET'])
def get_by_email():
    username = request.form.get('username')
    email = request.form.get('email')
    user=db.session.query(User).filter(or_(User.username==username,User.email==email)).first()
    res = user.__repr__()
    return res
    # if user:
    #     user.email=email
    #     db.session.commit()
    #     return 'update'
    # return 'Not update'
