#food-trucks

[Food Trucks Service](https://desolate-eyrie-6590.herokuapp.com/)

##Prompt
Create a service that tells the user what types of food trucks might be found near a specific location on a map.

The data is available on [DataSF: Food Trucks](https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat?)

##Solution
###Use Cases
As a user, some minimal functionalities I would want out of the food trucks service is
```
1. The ability to look at food truck options within .5 miles, 1 mile, 5 miles, etc. from exactly where I currently am.
2. The ability to procure a list of food trucks that serve the type of food that I want to eat right now. For example, today, I want tacos.
```
With these in mind, I set out to design the back end of this system. 

###Architecture
**Django REST Framework** for the service design. It scaffolds with boilerplate code and allows me to focus on important logic. I also chose it because it is written in Python and because it has a well-developed community of users.
```
**Heroku** for hosting. Django/Python is one of the main infrastructures/languages that it supports.
**SQLite** for development database. Queries are very fast and appropriate for development.
**PostgreSQL** for production database. This is provided for free by Heroku.
```

###Models

####FoodTrucks
This model represents the food trucks. It will have the most important data as its fields:
```
**name** CHAR from *Applicant* field
**address** CHAR from *Address* field
**fooditems** CHAR from *FoodItems* field
**longitude** DECIMAL from *Longitude* field
**latitude** DECIMAL from *Latitude* field
**foodtypes** MANYTOMANY foreign key into FoodTypes objects
```

####FoodTypes
This model represents the food types. There are 20 items that I pre-determined in FOOD_CHOICES tuple (*tacos, burgers, hot dogs,* etc.):

**food** INTEGER choices




*Relationship:*

FoodTrucks and FoodTypes have a many to many relationship. That way, we'll be able to realize the two functionalities I mentioned earlier. Query FoodTrucks on its *longitude* and *latitude*, and we should be able to get a filtered list of food trucks close by with major FoodTypes that it serves. Search for one of the major FoodTypes, and we should be able get all FoodTrucks that serve it.


###Files I Authored
**quickstart/models.py**

Holds the FoodTrucks and FoodTypes model. Represents the schema of the database as well.


**quickstart/management/commands/populate.py**

Used to populate initial data in the databases using a json-loadable text file. I used DataSF's FoodTrucks endpoint. I only processed records where the facilities had 'APPROVED' permit statuses. There were a lot of duplicate food trucks but I kept them anyway since some do seem to have different addresses and coordinates.

*Usage: python manage.py populate datasf.json* 


**quickstart/serializers.py**

Determines which FoodTrucks and FoodTypes fields are served when queried. 


**quickstart/tests.py**

Unit tests, written to test Views and Models which have custom functions in them.


**quickstart/views.py**
Determines the queryset that is returned for FoodTrucks and FoodTypes upon rquest.

FoodTrucksSerializer supports url query parameters to filter FoodTrucks based on longitude, latitude, and distance. For example, if given

>https://desolate-eyrie-6590.herokuapp.com/foodtrucks?longitude=-122.394594036205000000000000000000&latitude=37.787900097818100000000000000000&distance=2

the results returned will be filtered so that food trucks fall within 2 miles north, south, east, and west. Results are essentially bounded by a square. I decided to use LatLon Python Package to do geocoordinate math, since it can be used to calculate distance between points as well as determine a destination point based on an origin, trajectory and distance.


**tutorial/urls.py**

Binds URI to the views.


###Example queries
Get the API Root
>https://desolate-eyrie-6590.herokuapp.com/

Get all food types with restaurants listed under them
>https://desolate-eyrie-6590.herokuapp.com/foodtypes/

Get all food trucks and their information
>https://desolate-eyrie-6590.herokuapp.com/foodtrucks/

Get all food trucks within one mile of the coordinate
>https://desolate-eyrie-6590.herokuapp.com/foodtrucks?longitude=-122.394594036205000000000000000000&latitude=37.787900097818100000000000000000

Get all food trucks within 5 miles of the coordinate
>https://desolate-eyrie-6590.herokuapp.com/foodtrucks?longitude=-122.394594036205000000000000000000&latitude=37.787900097818100000000000000000&distance=5

###In the future

In the future, I want to implement these functions:
```
1. Ability to search FoodTrucks for any keywords in the fooditems key
2. Front-end using bootstrap and AngularJS
3. Implement some machine learning to  determine FoodType based off of the fooditems key, rather than using pre-determined FoodTypes.
4. Support filtering FoodTrucks by circular radius instead of box radius.
```

# More from me
[LinkedIn](https://www.linkedin.com/in/lynguyen60) - Everything about my professional experience and education

[lynguyen.me](http://www.lynguyen.me) - My projects and blogs will go up here. Currently I have a blog where I walk through my thought process and complexity analysis for a brain teaser I did in Python.

[Brain Teaser](https://github.com/lxn2/coding-challenges/blob/master/ExtraHop-knight-move-words-soln.py) - The brain teaser code that I mentioned above can be found here.

Happy browsing! :)