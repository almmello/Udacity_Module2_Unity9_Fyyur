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


#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#
import dateutil.parser
import babel

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime




