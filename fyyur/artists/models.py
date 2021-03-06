#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from fyyur import db


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    # genres changed to Array
    genres = db.Column('genres', db.ARRAY(db.String()), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # OK: implement any missing fields, as a database migration using Flask-Migrate
    # All missing fields added
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(500))
    
    # Changed relationship to lazy='joined', cascade="all, delete"
    shows = db.relationship('Show', backref='artist', lazy='joined', cascade="all, delete")

    def __repr__(self):
        return f'<Class ID: {self.id}, NAME: {self.name}, CITY: {self.city}>'

