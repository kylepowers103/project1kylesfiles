from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash

# initialize new Flask app
server = Flask(__name__)
# add configurations and database
server.config['DEBUG'] = True
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connect flask_sqlalchemy to the configured flask app
db = SQLAlchemy(server)

#create new Dash app and use existing Flask app as our Dash app's server
app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')
#import our routes after our database has been configured
from ourpackage.models import *
from ourpackage.routes import *
from ourpackage.dashboard import *
