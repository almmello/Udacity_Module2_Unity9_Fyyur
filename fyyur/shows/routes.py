#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import render_template, request, flash, redirect, url_for, Blueprint
from datetime import datetime
from fyyur.main.filters import format_datetime
from fyyur import db

#create the blueprint
shows_bp = Blueprint('shows_bp', __name__)

#adjusted the imports to package
from fyyur.shows.forms import *

#This was added to import models from shows
from fyyur.shows.models import Show

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

#Adjusted all decorators to use the blueprint

@shows_bp.route('/shows')
def shows():
# displays list of shows at /shows
# OK: replace with real venues data.
  #create variables data (will be passed to page shows) and shows (query).
  data = []
  shows = Show.query.order_by(db.desc(Show.start_time))

  #loop into shows to create the data dictionary for each show,
  for show in shows:
    data.append({
      'venue_id': show.venue_id,
      'venue_name': show.venue.name,
      'artist_id': show.artist_id,
      'artist_name': show.artist.name,
      'artist_image_link': show.artist.image_link,
      'start_time': format_datetime(str(show.start_time))
    })
    
  return render_template('pages/shows.html', shows=data)

@shows_bp.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@shows_bp.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # OK: insert form data as a new Show record in the db, instead

  # on successful db insert, flash success
  try:
    show = Show(
                start_time=request.form['start_time'],
                artist_id=request.form['artist_id'],
                venue_id=request.form['venue_id'],
                )

    db.session.add(show)
    db.session.commit()
    flash('Show was successfully listed!')

  # OK: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  except:
    db.session.rollback()
    flash('An error occurred. Show could not be listed.')
  finally:
    db.session.close()
  
  return render_template('pages/home.html')

