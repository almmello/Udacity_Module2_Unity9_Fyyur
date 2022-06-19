#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

#Import the Config class
from config import Config

moment = Moment(app)

#Changed to the class Config
app.config.from_object(Config)

db = SQLAlchemy(app)

# TODO: connect to a local postgresql database

#Import Routes
from fyyur import routes

#Import Filters
from fyyur import filters






