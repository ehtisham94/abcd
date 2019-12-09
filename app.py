import random
from flask import Flask,render_template, request

print(__file__)

import os
project_dir = os.path.dirname(os.path.abspath(__file__))
myApp =  Flask(__name__)

print(project_dir)

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

myApp.config["SQLALCHEMY_DATABASE_URI"] = database_file
myApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



db = SQLAlchemy(myApp)

# db.create_all()

class User(db.Model):

    id = db.Column(db.Integer,unique=True, nullable=False, primary_key = True, autoincrement=True)
    name = db.Column(db.String(50),unique=False, nullable=False)
    email = db.Column(db.String(50),unique=True, nullable=False)
    status = db.Column(db.String(1),unique=False, nullable=False)
    password = db.Column(db.String(50),unique=False, nullable=False)


    # name = db.Column(db.String(40),unique=True, nullable=False, primary_key = True)
    # password = db.Column(db.String(40),unique=False, nullable=False)
    # city = db.Column(db.String(40),unique=False, nullable=False)

# db.create_all()

@myApp.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        if User.query.filter_by(email = request.form['email']).first() :
            return render_template('signup.html',msgs=["Email already exist"])
        else:
            user1 = User()
            user1.name = request.form['name']
            user1.email = request.form['email']
            user1.status = request.form['status']
            user1.password = random.randint(1000, 9999)
            db.session.add(user1)
            db.session.commit()
            return render_template('signup.html', msgs=[" Successfull ", "Email : "+ user1.email, "Password : "+ user1.password] )
    else:
        return render_template('signup.html')

@myApp.route('/users')
def users():
    myUsers = User.query.all()
    return render_template('users.html', users=myUsers)

@myApp.route('/delete', methods=["POST"])
def delete_user():
    user_id = request.form['id']

    user_found = User.query.filter_by(id=user_id).first()

    db.session.delete(user_found)
    db.session.commit()

    myUsers = User.query.all()

    return render_template('users.html', users=myUsers)

@myApp.route('/update', methods=["POST"])
def update_user():
    user_id = request.form['id']
    user_name = request.form['name']
    user_pass = request.form['password']

    user_found = User.query.filter_by(id=user_id).first()

    user_found.name = user_name
    user_found.password = user_pass

    db.session.add(user_found)
    db.session.commit()

    myUsers = User.query.all()

    return render_template('users.html', users=myUsers)

@myApp.route('/')
def index():

    return render_template('login.html', ty="ACCOUNT", ac="login")
    # return render_template('index.html')

@myApp.route('/login', methods=["POST", "GET"])
def login():

    if request.method == "POST":
        # print ("user"+request.path)
        u = User.query.filter_by(email = request.form['username']).first()
        if u :
            if u.email == request.form['username'] and u.password == request.form['pass']:
                if u.status == 'A':
                    return render_template('adminpanle.html')
                elif u.status == 'T':
                    return render_template('dashboard.html', msgs=["Welcome Teacher","Name : "+u.name, "Email : "+u.email, "Password : "+u.password])
                elif u.status == 'S':
                    return render_template('dashboard.html', msgs=["Welcome Student","Name : "+u.name, "Email : "+u.email, "Password : "+u.password])
            else:
                return render_template('login.html', ty="ACCOUNT", ac="login", msg="Invalid credentials ! ")
        else:
            return render_template('login.html', ty="ACCOUNT", ac="login", msg="Invalid credentials ! ")
    else :
        return render_template('login.html', ty="ACCOUNT", ac="login")
        # return render_template('login.html', ty="USER", ac="login")


    #return "<h1>Hello login!</h1><h1>Hello login!</h1><h1>Hello login!</h1>"


@myApp.route('/admin', methods=["POST", "GET"])
def admin():
    error = None
    if request.method == "POST":
        # print ("admin" + request.path)
        a = User.query.filter_by(status="A").first()
        if request.form['username'] == a.email and request.form['pass'] == a.password:
            return render_template('adminpanle.html')
        else:
            return render_template('login.html', ty="ADMIN", ac="admin", msg="Invalid credentials ! ")
        # return render_template('login.html', ty="ADMIN", ac="admin")
    else:
        return render_template('login.html', ty="ADMIN", ac="admin")





@myApp.route('/adminpanle', methods=["POST"])
def adminpanle():
    return render_template('adminpanle.html')


@myApp.route('/test1', methods=["POST", "GET"])
def mySignup():
    # print(request.form['username'])

    if request.method == "POST":
        user1 = User()
        user1.name = request.form['username']
        user1.password = request.form['pass']
        user1.city = request.form['city']

        db.session.add(user1)
        db.session.commit()

    return render_template('signup.html')



# print(__name__)

# if __name__ == "__main__":
# myApp.run(debug=True)
# myApp.run()


