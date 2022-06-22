#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import render_template, request, flash, redirect, url_for, Blueprint
from fyyur.main.filters import format_datetime
from fyyur import db
import sys

#create the blueprint
artists_bp = Blueprint('artists_bp', __name__)

#adjusted the imports to package
from fyyur.artists.models import Artist
from fyyur.shows.models import Show
from fyyur.artists.forms import *

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

#Adjusted all decorators to use the blueprint

@artists_bp.route('/artists')
def artists():
  # OK: replace with real data returned from querying the database
  #create variables data (will be passed to page artist) and artists (query).
  data = []
  artists = Artist.query.all()
  
  #loop into artists to create the data dictionary for each artist,
  for artist in artists:
    data.append({
      "id": artist.id,
      "name": artist.name
    })
  return render_template('pages/artists.html', artists=data)


@artists_bp.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  # OK: replace with real artist data from the artist table, using artist_id
  # Create variables artists (query with <id>), shows (query with artist <id>),
  # past shows and upcaming shows.
  artist = Artist.query.get(artist_id)
  shows = Show.query.filter_by(artist_id=artist_id).all()
  past_shows = []
  upcoming_shows = []

  # loop through shows to set the past and upcoming shows lists
  #create variables data (will be passed to page venues/<int>)
  for show in shows:
    data = {
      'venue_id': show.venue_id,
      'venue_name': show.venue.name,
      'venue_image_link': show.venue.image_link,
      'start_time': format_datetime(str(show.start_time))
    }
    if show.start_time < datetime.now():
      past_shows.append(data)
    else:
      upcoming_shows.append(data)

  # add values to data dictionary
  data = {
    'id': artist.id,
    'name': artist.name,
    'genres': artist.genres,
    'city': artist.city,
    'state': artist.state,
    'phone': artist.phone,
    'website': artist.website,
    'facebook_link': artist.facebook_link,
    'seeking_venue': artist.seeking_venue,
    'seeking_description':artist.seeking_description,
    'image_link': artist.image_link,
    'past_shows': past_shows,
    'upcoming_shows': upcoming_shows,
    'past_shows_count': len(past_shows),
    'upcoming_shows_count': len(upcoming_shows)
  }

  return render_template('pages/show_artist.html', artist=data)

#  Create Artist
#  ----------------------------------------------------------------

@artists_bp.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)


@artists_bp.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # OK: insert form data as a new Artist record in the db, instead
  # OK: modify data to be the data object returned from db insertion

  # Using the try-except-finally pattern.
  try:
    # first we create a form instance with the data from the submited form
    form = ArtistForm()

    # then we create an artist object with data from the form matching the table Artist
    artist = Artist(
                     name=form.name.data,
                     city=form.city.data,
                     state=form.state.data,
                     phone=form.phone.data,
                     genres=form.genres.data,
                     image_link=form.image_link.data,
                     facebook_link=form.facebook_link.data,
                     website=form.website_link.data,
                     seeking_venue=form.seeking_venue.data,
                     seeking_description=form.seeking_description.data
                     )

    # now, we add the artist object into database
    db.session.add(artist)

    # to persist the data on the database, we than commit the db session
    db.session.commit()

  # OK: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
    flash('Artist ' + request.form['name'] + ' was successfully listed!')

  except:
    # in case of an error, we rollback the session and flash error
    db.session.rollback()
    flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
    # print stack trace for an exception
    print(sys.exc_info())
  finally:
    # last thing we do, close the session and return to the home page
    db.session.close()
  return render_template('pages/home.html')


@artists_bp.route('/artists/search', methods=['POST'])
def search_artists(): 
# OK: implement search on artists with partial string search. Ensure it is case-insensitive.
# seach for "a" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
# search for "Band" should return "The Wild Sax Band".

  # Get the search term from the form using GET
  search_term = request.form.get('search_term', '')

    # Quering the table Artists using a filter with the search_term between wilcard (%) and ilike to be case-sensitive
  artists_query = Artist.query.filter(Artist.name.ilike(f'%{search_term}%'))

  # Finally we create the response by using the function count on the query results and sending the result as a dictionary
  response = {
    'count': artists_query.count(),
    'data': artists_query
  }

  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))


#  Update
#  ----------------------------------------------------------------
@artists_bp.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()

  # Quering the database using artist_id from the URL
  artist_query = Artist.query.get(artist_id)

  # Then we create the response dictionary, artist, with the artist_id and with the artist_query itens
  artist={
    "id": artist_id,
    "name": artist_query.name,
    "genres": artist_query.genres,
    "city": artist_query.city,
    "state": artist_query.state,
    "phone": artist_query.phone,
    "website": artist_query.website,
    "facebook_link": artist_query.facebook_link,
    "seeking_venue": artist_query.seeking_venue,
    "seeking_description": artist_query.seeking_description,
    "image_link": artist_query.image_link
  }

# OK: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)


@artists_bp.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
# OK: take values from the form submitted, and update existing
# artist record with ID <artist_id> using the new attributes

  # Using the try-except-finally pattern.
  try:
    # first we create a form instance with the data from the submited form
    form = ArtistForm()

    # then we create a artist_query instance using the artist_id from URL
    artist_query = Artist.query.get(artist_id)

    # and then we update the artist_query instance with the data from the form instance
    artist_query.name = form.name.data
    artist_query.city = form.city.data
    artist_query.state = form.state.data
    artist_query.phone = form.phone.data
    artist_query.genres = form.genres.data
    artist_query.image_link = form.image_link.data
    artist_query.facebook_link = form.facebook_link.data
    artist_query.website = form.website_link.data
    artist_query.seeking_venue = form.seeking_venue.data
    artist_query.seeking_description = form.seeking_description.data

    # to persist the data on the database, we than commit the db session
    db.session.commit()

    # after that, we flash success with the artist name
    flash('Artist ' + form.name.data + ' was successfully updated!')

  except:
    # in case of an error, we rollback the session and flash error
    db.session.rollback()
    flash('An error occurred. Artist ' + form.name.data + ' could not be updated.')

    # print stack trace for an exception
    print(sys.exc_info())

  finally:
    # last thing we do, close the session and return with the artist page
    db.session.close()
  return redirect(url_for('artists_bp.show_artist', artist_id=artist_id))




