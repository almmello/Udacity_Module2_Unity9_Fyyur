import os

class Config(object):
    SECRET_KEY = os.urandom(32)
    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Enable debug mode.
    DEBUG = True

    # Set SQLALCHEMY Track Notifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # OK IMPLEMENT DATABASE URL
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/fyyurdb'
