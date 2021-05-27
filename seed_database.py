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
# Create movies, store them in list so we can use them
# to create fake ratings later


movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    title, overview, poster_path = (movie['title'],
                                    movie['overview'],
                                    movie['poster_path'])
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d' )

    # TODO: create a movie here and append it to movies_in_db
#movie_data will be a list of dictionaries that look like this:
    db_movie = crud.create_movie(title,
                                overview,
                                release_date,
                                poster_path)

    movies_in_db.append(db_movie)

#Loop over each dictionary in movie_data and use it to supply 
#arguments to crud.create_movie.  
#add each new movie to a list  
#to create random ratings.  
#work with the db.DateTime column-type 

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # TODO: create a user here
    user = crud.create_user(email, password) 
    # TODO: create 10 ratings for the user
    for _ in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        crud.create_rating(user, random_movie, score)

