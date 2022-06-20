#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import render_template, request, flash, redirect, url_for, Blueprint
from fyyur import app

import logging
from logging import Formatter, FileHandler

#create the blueprint
main_bp = Blueprint('main_bp', __name__)

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

#Adjusted all decorators to use the blueprint

@main_bp.route('/')
def index():
  return render_template('pages/home.html')


@main_bp.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@main_bp.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')