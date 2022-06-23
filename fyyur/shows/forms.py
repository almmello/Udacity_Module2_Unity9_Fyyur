#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired, Length

#----------------------------------------------------------------------------#
# Forms.
#----------------------------------------------------------------------------#

class ShowForm(Form):
    artist_id = StringField(
        # Added Lenght Validation
        'artist_id', validators=[DataRequired(), Length(max=10, message=('Maximum Artist ID size is 10 characters!'))]
    )
    venue_id = StringField(
        # Added Lenght Validation
        'venue_id', validators=[DataRequired(), Length(max=10, message=('Maximum Venue ID size is 10 characters!'))]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today(), 
    )

