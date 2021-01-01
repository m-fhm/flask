from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'
# ap.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
@app.route('/<name>/<email>')
def index(name,email):
    user = User(username=name,email=email)
    db.session.add(user)
    db.session.commit()
    return'<h1> added new user</h1>'
@app.route('/<name>')
def show(name):
    user = User.query.filter_by(username=name).first()

    return f'<h1> added new user{user.email}</h1>'
# @app.route('/')
# def index():
#     return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)