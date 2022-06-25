#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import (
                   render_template,
                   flash,
                   Blueprint,
                   request
                  )
from sqlalchemy import or_
from fyyur.main.filters import format_datetime
from fyyur import db
import sys

#create the blueprint
shows_bp = Blueprint('shows_bp', __name__)

#adjusted the imports to package
from fyyur.shows.forms import *

#This was added to import models from shows
from fyyur.shows.models import Show
from fyyur.artists.models import Artist
from fyyur.venues.models import Venue

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

  # first we create a form instance with the data from the submited form
  form = ShowForm(request.form)

  # Using the try-except-finally pattern.
  try:

    # then we create a show object
    show = Show()

    # To avoid having to deal with each field manually,
    # we use the form.populate_obj() method:
    form.populate_obj(show)

    # now, we add the artist object into database
    db.session.add(show)

    # to persist the data on the database, we than commit the db session
    db.session.commit()

    # then we flash success
    flash('Show was successfully listed!')

  # OK: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  except:
    db.session.rollback()
    flash('An error occurred. Show could not be listed.')
    # print stack trace for an exception
    print(sys.exc_info())

  finally:
    # last thing we do, close the session and return to the home page
    db.session.close()

  return render_template('pages/home.html')


@shows_bp.route('/shows/search', methods=['POST'])
def search_shows(): 
# OK: implement search on shows with partial string search. Ensure it is case-insensitive.
# seach for "a" will return shows with artists or venues containig the letter "a"


  # Get the search term from the form using GET
  search_term = request.form.get('search_term', '')

  # Quering the table Shows join Artist join Venue using a filter with the search_term between wilcard (%) and ilike to be case-sensitive
  shows_query = db.session.query(Show.id, Show.artist_id, Show.venue_id, Show.start_time, Artist.name, Artist.image_link, Venue.name).join(Artist).join(Venue).filter(or_(Artist.name.ilike(f'%{search_term}%'), Venue.name.ilike(f'%{search_term}%')))

  # Finally we create the response by using the function count on the query results and sending the result as a dictionary
  response = {
    'count': shows_query.count(),
    'data': shows_query.all()
  }

  return render_template('pages/search_shows.html', results=response, search_term=request.form.get('search_term', ''))