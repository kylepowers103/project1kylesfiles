from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import dash

app = Flask(__name__)
# add configurations and database URI
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
