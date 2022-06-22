#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import render_template, request, flash, redirect, url_for, Blueprint
from fyyur import app, db
from datetime import datetime
from fyyur.main.filters import format_datetime
import sys

#create the blueprint
venues_bp = Blueprint('venues_bp', __name__)

#adjusted the imports to package
from fyyur.venues.models import Venue
from fyyur.shows.models import Show
from fyyur.venues.forms import *

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

#Adjusted all decorators to use the blueprint

@venues_bp.route('/venues')
def venues():
  # OK: replace with real venues data.
  # num_upcoming_shows should be aggregated based on number of upcoming shows per venue. OK
  # create variables data (will be passed to page venues/<id>),
  # venues (query), shows (query) and locations to add into data.
  data = []
  venues = Venue.query.all()
  shows = Show.query.all()
  locations = set()
  
  # loop into venues to create a list of all locations.
  for venue in venues:
    locations.add((venue.city, venue.state))

  # loop into locations to create the data dictionary for each location,
  # leaving a space to add venues in the next step.
  for location in locations:
    data.append({
      "city": location[0],
      "state": location[1],
      "venues": []
    })

  # loop into venues
  for venue in venues:
    # loop into data
    for location in data:
      # reset the num_upcoming_shows
      num_upcoming_shows = 0
      # if the venue location is equal to the venue in data, then add the venue (id and name)
      # into a dictionary inside the location in the data
      if venue.city == location['city'] and venue.state == location['state']:
        # loop into shows to find the num_upcoming_shows
        for show in shows:
          if show.venue_id == venue.id and show.start_time > datetime.now():
            num_upcoming_shows += 1

        location['venues'].append({
          "id": venue.id,
          "name": venue.name,
          "num_upcoming_shows": num_upcoming_shows
        })
        print(location)

  # finally return data as areas to venues.html page
  return render_template('pages/venues.html', areas=data);

@venues_bp.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # OK: replace with real venue data from the venues table, using venue_id
  # Create variables venues (query with <id>), shows (query with venue <id>),
  # past shows and upcaming shows.
  venue = Venue.query.get(venue_id)
  shows = Show.query.filter_by(venue_id=venue_id).all()
  past_shows = []
  upcoming_shows = []

  # loop through shows to set the past and upcoming shows lists
  #create variables data (will be passed to page venues/<int>)
  for show in shows:
    data = {
      "artist_id": show.artist_id,
      "artist_name": show.artist.name,
      "artist_image_link": show.artist.image_link,
      "start_time": format_datetime(str(show.start_time))
    }
    if show.start_time < datetime.now():
      past_shows.append(data)
    else:
      upcoming_shows.append(data)

  # add values to data dictionary
  data={
    "id": venue.id,
    "name": venue.name,
    "genres": venue.genres,
    "address": venue.address,
    "city": venue.city,
    "state": venue.state,
    "phone": venue.phone,
    "website": venue.website,
    "facebook_link": venue.facebook_link,
    "seeking_talent": venue.seeking_talent,
    "seeking_description":venue.seeking_description,
    "image_link": venue.image_link,
    "past_shows": past_shows,
    "upcoming_shows": upcoming_shows,
    "past_shows_count": len(past_shows),
    "upcoming_shows_count": len(upcoming_shows)
  }

  return render_template('pages/show_venue.html', venue=data)

@venues_bp.route('/venues/search', methods=['POST'])
def search_venues():
  # OK: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"

  # Get the search term from the form using GET
  search_term = request.form.get('search_term', '')

  # Quering the table Venue using a filter with the search_term between wilcard (%) and ilike to be case-sensitive
  venues_query = Venue.query.filter(Venue.name.ilike(f'%{search_term}%'))

  # Finally we create the response by using the function count on the query results and sending the result as a dictionary
  response={
    "count": venues_query.count(),
    "data": venues_query
  }

  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))


#  Create Venue
#  ----------------------------------------------------------------

@venues_bp.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)


@venues_bp.route('/venues/create', methods=['POST'])
def create_venue_submission():
# OK: insert form data as a new Venue record in the db, instead
# OK: modify data to be the data object returned from db insertion

  # Using the try-except-finally pattern.
  try:
    # first we create a form instance with the data from the submited form
    form = VenueForm()

    # then we create a venue object with data from the form matching the table Venue
    venue = Venue(
                  name=form.name.data,
                  city=form.city.data,
                  state=form.state.data,
                  address=form.address.data,
                  phone=form.phone.data,
                  image_link=form.image_link.data,
                  facebook_link=form.facebook_link.data,
                  genres=form.genres.data,
                  website=form.website_link.data,
                  seeking_talent=form.seeking_talent.data,
                  seeking_description=form.seeking_description.data
                  )

    # now, we add the venue object into database
    db.session.add(venue)

    # to persist the data on the database, we than commit the db session
    db.session.commit()

# OK: on unsuccessful db insert, flash an error instead.
# e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
# see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    flash('Venue ' + request.form['name'] + ' was successfully listed!')

  except:
    # in case of an error, we rollback the session and flash error
    db.session.rollback()
    flash('An error occurred. Venue ' + request.form['name']  + ' could not be listed.')
    # print stack trace for an exception
    print(sys.exc_info())
  finally:
    # last thing we do, close the session and return to the home page
    db.session.close()
  return render_template('pages/home.html')


@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # OK: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.

  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage

  # Using the try-except-finally pattern.
  try:
    # first we create a venue instance using the venue_id from URL
    venue = Venue.query.get(venue_id)

    # then we delete the venue
    db.session.delete(venue)

    # to persist the data on the database, we than commit the db session
    db.session.commit()

    # after that, we flash success with the venue name
    flash('Venue ' + venue.name + ' was deleted')
  except:
    # in case of an error, we rollback the session and flash error
    db.session.rollback()
    flash('An error occurred. Venue ' + venue.name + ' could not be deleted.')

    # print stack trace for an exception
    print(sys.exc_info())

  finally:
    # last thing we do, close the session and return to home page
    db.session.close()
  return render_template('pages/home.html')



@venues_bp.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()

  # Quering the database using venue_id from the URL
  venue_query = Venue.query.get(venue_id)

  # Then we create the response dictionary, venue, with the venue_id and with the venue_query itens
  venue = {
    "id": venue_id,
    "name": venue_query.name,
    "genres": venue_query.genres,
    "address": venue_query.address,
    "city": venue_query.city,
    "state": venue_query.state,
    "phone": venue_query.phone,
    "website":venue_query.website,
    "facebook_link": venue_query.facebook_link,
    "seeking_talent": venue_query.seeking_talent,
    "seeking_description": venue_query.seeking_description,
    "image_link": venue_query.image_link
  }  
  
  # OK: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)


@venues_bp.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
# OK: take values from the form submitted, and update existing
# venue record with ID <venue_id> using the new attributes

  # Using the try-except-finally pattern.
  try:
    # first we create a form instance with the data from the submited form
    form = VenueForm()

    # then we create a venue_query instance using the venue_id from URL
    venue_query = Venue.query.get(venue_id)

    # and then we update the venue_query instance with the data from the form instance
    venue_query.name = form.name.data
    venue_query.city = form.city.data
    venue_query.state = form.state.data
    venue_query.address = form.address.data
    venue_query.phone = form.phone.data
    venue_query.image_link = form.image_link.data
    venue_query.facebook_link = form.facebook_link.data
    venue_query.genres = form.genres.data
    venue_query.website = form.website_link.data
    venue_query.seeking_talent = form.seeking_talent.data
    venue_query.seeking_description = form.seeking_description.data

    # to persist the data on the database, we than commit the db session
    db.session.commit()

    # after that, we flash success with the venue name
    flash('Venue ' + form.name.data + ' was successfully updated!')

  except:
    # in case of an error, we rollback the session and flash error
    db.session.rollback()
    flash('An error occurred. Venue ' + form.name.data + ' could not be updated.')

    # print stack trace for an exception
    print(sys.exc_info())

  finally:
    # last thing we do, close the session and return with the venue page
    db.session.close()
  return redirect(url_for('venues_bp.show_venue', venue_id=venue_id))

