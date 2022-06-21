#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
# Ading Flask-Migrate
from flask_migrate import Migrate

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
#Adding Migrate
migrate = Migrate(app, db)

# OK: connect to a local postgresql database
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI

#Import Routes as Blueprints
from fyyur.artists.routes import artists_bp
from fyyur.main.routes import main_bp
from fyyur.shows.routes import shows_bp
from fyyur.venues.routes import venues_bp

app.register_blueprint(artists_bp)
app.register_blueprint(main_bp)
app.register_blueprint(shows_bp)
app.register_blueprint(venues_bp)


#Import Filters
from fyyur.main import filters






