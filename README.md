# Moviews-API

This project is a movie rating system, admins can add movies and users can add reviews.\
The API returns the movies and ratings.

# Running backend server

#### Clone this repository
```
$ git clone <https://github.com/gilsongindrejr/Moviews-API.git>
```

#### Access the project folder
```
$ cd Moviews
```

#### Activate the virtual enviroment
```
$ source venv/bin/activate
```

#### Install requirements
```
$ pip install -r requirements.txt
```

#### Migrate the database
```
$ python manage.py migrate
```

#### Run server
```
$ python manage.py runserver
```

#### The server will be initiated on port 8000 - access <http://127.0.0.1:8000> 

# Endpoints

#### Movies

<http://127.0.0.1:8000/api/v1/movies/>

the movie id can be passed to retrieve a specific movie, like:\
<http://127.0.0.1:8000/api/v1/movies/1/>

To retrieve the movie ratings, use:\
<http://127.0.0.1:8000/api/v1/movies/1/ratings/>

#### Ratings

<http://127.0.0.1:8000/api/v1/ratings/>

The rating id can be passed to retrieve a specific rating, like:\
<http://127.0.0.1:8000/api/v1/ratings/1/>
