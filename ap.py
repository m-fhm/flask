from flask import Flask
from flask_sqlalchemy import SQLAlchemy
ap=Flask(__name__)
ap.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'
ap.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(ap)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
@ap.route('/<name>/<email>')
def index(name,email):
    user = User(username="adfaf",email=email)
    db.session.add(user)
    db.session.commit()
    return'<h1> added new user</h1>'
@ap.route('/<name>')
def show(name):
    user = User.query.filter_by(username=name).first()

    return f'<h1> added new user{user.email}</h1>'
if __name__ == "__main__":
    ap.run(debug=True)