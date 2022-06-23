#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired, URL, Length

#----------------------------------------------------------------------------#
# Forms.
#----------------------------------------------------------------------------#

class ArtistForm(Form):
    name = StringField(
        # Added Lenght Validation
        'name', validators=[DataRequired(), Length(max=110, message=('Maximum Name size is 110 characters!'))]
    )
    city = StringField(
        # Added Lenght Validation
        'city', validators=[DataRequired(), Length(max=110, message=('Maximum City size is 110 characters!'))]
    )
    state = SelectField(
        # Added Lenght Validation
        'state', validators=[DataRequired()],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    phone = StringField(
        # OK implement validation logic for state
        # Added Lenght Validation
        'phone', validators=[DataRequired(), Length(max=20, message=('Maximum Phone size is 20 characters!'))]
    )
    image_link = StringField(
        # Added Lenght Validation
        'image_link', validators=[DataRequired(), Length(max=490, message=('Maximum Image Link size is 490 characters!'))]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=[
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other'),
        ]
     )
    facebook_link = StringField(
        # OK implement enum restriction
        # It is not necessary to implement Enom, as on https://knowledge.udacity.com/questions/800921
        # "the forms are already implementing a list that restricts genres."
        # Facebook links are also validated using the URL validator.
        # Added Lenght Validation
        'facebook_link', validators=[URL(), Length(max=110, message=('Maximum Facebook Link size is 110 characters!'))]
     )

    website_link = StringField(
        # Added Lenght Validation
        'website_link', validators=[DataRequired(), Length(max=110, message=('Maximum Website Link size is 110 characters!'))]
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
        # Added Lenght Validation
        'seeking_description', validators=[DataRequired(), Length(max=490, message=('Maximum Seeking Description size is 490 characters!'))]
     )

