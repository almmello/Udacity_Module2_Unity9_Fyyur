#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from fyyur import db
from datetime import datetime

#This was added to import models from artists and venues
from fyyur.artists.models import Artist
from fyyur.venues.models import Venue



#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
# OK Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
# Show model created with relationships and properties

class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)

    def __repr__(self):
        return f'<Class ID: {self.id}, START_TIME: {self.start_time}, ARTIST_ID: {self.artist_id}>'
