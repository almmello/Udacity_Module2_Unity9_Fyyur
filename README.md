Fyyur
-----

## My Release

This repository is my version of the Fyyur app (https://github.com/udacity/cd0046-SQL-and-Data-Modeling-for-the-Web).
I recorded my development through commits so that you can follow along.
Aside from the basic requirements, I have migrated the whole project into a package structure to satisfy the Separation of Concerns; Then, I have migrated into Blueprints to better separate the Packages.
Please let me know if you find any issues with this project.

## Requirements Adjustments

It was necessary to set Jinja2 and Werkzeug versions on requirements.txt as follows:
```
Jinja2==3.0.0
Werkzeug==2.0.3
```

## References

During the development, I used the following references to build the Fyyur app:

https://flask-wtf.readthedocs.io/en/1.0.x/
https://flask.palletsprojects.com/en/2.1.x/
https://flask.palletsprojects.com/en/2.1.x/patterns/packages/
https://flask.palletsprojects.com/en/1.0.x/patterns/flashing/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#
https://flask-migrate.readthedocs.io/en/latest/
https://flask-moment.readthedocs.io/en/latest/quickstart.html#installation-and-configuration
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
https://en.wikipedia.org/wiki/Separation_of_concerns
https://docs.python.org/3/tutorial/modules.html#importing-from-a-package
https://www.youtube.com/watch?v=44PvX0Yv368&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=6
https://www.youtube.com/watch?v=-BC3V1CUKpU
https://www.linkedin.com/learning/full-stack-web-development-with-flask/
https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore
https://stackoverflow.com/questions/58532518/why-flask-migrations-does-not-detect-a-fields-length-change

## Introduction

Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as venue owners.

I have built the data models to power the API endpoints for the Fyyur site by connecting to a PostgreSQL database for storing, querying, and creating information about artists and venues on Fyyur.

## Overview

This app is capable of doing the following using a PostgreSQL database:

* creating new venues and artists and creating new shows.
* searching for venues, artists, and shows.
* Learning more about a specific artist or venue.

We want Fyyur to be the next new platform that artists and musical venues can use to find each other and discover new music shows!

## Tech Stack (Dependencies)

### 1. Backend Dependencies
Our tech stack includes the following:
 * **virtualenv** as a tool to create isolated Python environments
 * **SQLAlchemy ORM** to be our ORM library of choice
 * **PostgreSQL** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 * **Flask-Migrate** for creating and running schema migrations

### 2. Frontend Dependencies
You must have the **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's frontend. Bootstrap can only be installed by Node Package Manager (NPM). Therefore, if not already, download and install the [Node.js](https://nodejs.org/en/download/). Windows users must run the executable as an Administrator and restart the computer after installation. After successfully installing the Node, verify the installation as shown below.
```
node -v
npm -v
```
Install [Bootstrap 3](https://getbootstrap.com/docs/3.3/getting-started/) for the website's frontend:

``` 
npm init -y
npm install bootstrap@3
```
## Run the App

First, create the database on your local Postgres installation.
```
createdb fyyurdb	  
```
Then edit the config.py file and adjust your SQLALCHEMY_DATABASE_URI, if necessary.

You can download and install the dependencies mentioned above using `pip` as:
```
pip install virtualenv
python3 -m venv venv 	  
source venv/bin/activate
pip install -r requirements.txt	  
```

Run the App:
```
export FLASK_APP=run.py	 
export FLASK_ENV=development	 
python3 -m flask run 	 
```  

## Main Files: Project Structure

├── LICENSE.txt
├── README.md
├── config.py
├── error.log
├── fyyur
│   ├── __init__.py
│   ├── artists
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── routes.py
│   ├── main
│   │   ├── filters.py
│   │   └── routes.py
│   ├── shows
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── routes.py
│   ├── static
│   │   ├── css
│   │   ├── fonts
│   │   ├── img
│   │   └── js
│   ├── templates
│   │   ├── errors
│   │   ├── forms
│   │   ├── layouts
│   │   └── pages
│   └── venues
│       ├── __init__.py
│       ├── forms.py
│       ├── models.py
│       └── routes.py
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── requirements.txt
├── run.py
  ```

Overall:
* Models are located in the "models.py" inside each package.
* Controllers are located in "routes.py" inside each package.
* The web frontend is located in "templates/", which builds static assets deployed to the web server at "static/".
* Web forms for creating data are located in "forms.py" inside each package.


Highlight folders:
* "templates/pages" -- Defines the pages rendered to the site. These templates render views based on data passed into the template's view in the controllers defined in routes files. These pages successfully represent the data to the user.
* "templates/layouts" -- Defines the layout in which a page can be contained to define the footer and header code for a given page.
* "templates/forms" -- Defines the forms used to create new artists, shows, and venues.
* "routes.py" -- Defines routes that match the user's URL and controllers which handle data and render views to the user. This is the main file connecting to and manipulating the database and rendering views with data to the user based on the URL.
* "models.py" -- Defines the database tables' data models.
* "config.py" -- Stores configuration variables and instructions, separate from the main application code. This is where you will need to connect to the database.

Achievements
-----

1. Understand the Project Structure and where important files are located. => OK
2. Build and run local development => OK
3. Fill in the missing functionality in this application: this application currently pulls in fake data and needs to now connect to an actual database and talk to a real backend. => OK
4. Fill out every "TODO" section throughout the codebase.
    * Connect to a database in "config.py". A project submission that uses a local database connection is acceptable. => OK
    * Using SQLAlchemy, set up normalized models for the objects we support in our web app in the Models section of "app.py". Check out the sample pages provided at /artists/1, /venues/1, and /shows for examples of the data we want to model, using all of the learned best practices in database schema design. Finally, implement missing model properties and relationships using database migrations via Flask-Migrate. => OK
    * Implement form submissions for creating new Venues, Artists, and Shows. Proper constraints should power the "/create" endpoints that serve the create form templates to avoid duplicate or nonsensical form submissions. In addition, submitting a form should create accurate new records in the database. => OK
    * Implement the controllers for listing venues, artists, and shows. Note the structure of the mock data used. We want to keep the structure of the mock data. => OK
    * Implement search, powering the "/search" endpoints that serve the application's search functionalities. => OK
    * Serve venue and artist detail pages, powering the "<venue|artist>/<id>" endpoints that power the detail pages. => OK

#### Data Handling with `Flask-WTF` Forms
The starter codes use an interactive form builder library called [Flask-WTF](https://flask-wtf.readthedocs.io/). This library provides useful functionality, such as form validation and error handling. You can peruse the Show, Venue, and Artist form builders in the "forms.py" file. The WTForms are instantiated in the "routes.py" file. For example, in the "create_shows()" function, the Show form is instantiated from the command: "form = ShowForm()". To manage the request from the Flask-WTF form, each field from the form has a "data" attribute containing the value from user input. For example, to handle the "venue_id" data from the Venue form, you can use: "show = Show(venue_id=form.venue_id.data)", instead of using "request.form['venue_id']".