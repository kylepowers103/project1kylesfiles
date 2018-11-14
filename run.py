# import Flask and jsonify from flask
from flask import Flask, jsonify
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import * #Column, Integer, String, ForeignKey, DateTime, create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from ourpackage import db
from ourpackage.models import Game,Team,Statistics
from ourpackage.routes  import *

#define routes and their respective functions that return the correct data
# remember that each function must have a unique name

# run the server
if __name__ == "__main__":
    app.run()
