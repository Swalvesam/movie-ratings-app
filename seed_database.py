"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
# More code will go here
#write as a script. What this means for you is that you won’t 
#have to define functions! Sounds scary, we know, 
#but this file will only be used to re-create your database.
#re-creating a database is run dropdb and createdb. 
#You can get Python to run those commands for you using os.system. 
#Add the following lines of code to seed_database.py.


os.system('dropdb ratings')
os.system('createdb ratings')


#connect to the database and call db.create_all:
#have to go through model before you can access db.
model.connect_to_db(server.app)
model.db.create_all()

#load data from data/movies.json and save it to a variable:
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

#movie_data will be a list of dictionaries that look like this:

#Loop over each dictionary in movie_data and use it to supply 
#arguments to crud.create_movie. You’ll also going to want to 
#add each new movie to a list because we’re going to need them 
#later to create random ratings.  
#we need to work with the db.DateTime column-type 


