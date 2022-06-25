#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from fyyur import db
from datetime import datetime

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # OK: implement any missing fields, as a database migration using Flask-Migrate
    # All missing fields added
    genres = db.Column('genres', db.ARRAY(db.String()), nullable=False)
    website = db.Column(db.String(250))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(250))

    # Changed relationship to lazy='joined', cascade="all, delete"
    shows = db.relationship('Show', backref='venue', lazy='joined', cascade="all, delete")

    def __repr__(self):
        return f'<Class ID: {self.id}, NAME: {self.name}, CITY: {self.city}>'
