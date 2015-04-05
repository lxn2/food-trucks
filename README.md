#food-trucks

##Prompt
###SF Movies

Create a service that shows on a map where movies have been filmed in San Francisco. The user should be able to filter the view using autocompletion search.

The data is available on [DataSF: Film Locations](https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am?).

##Solution
###Use Cases
As a user, some minimal functionalities I would want out of the food trucks service is
1) The ability to look at food truck options within .5 miles, 1 mile, 5 miles, etc. from exactly where I current am.
2) The ability to procure a list of food trucks that serve the type of food that I want to eat right now. Today, I want tacos.

With these in mind, I set out to design the back end of this system. 

###Architecture
**Django REST Framework** for the service design. It scaffolds with boilerplate code and allows me to focus on important logic. I also chose it because it is written in Python and because it has a well-developed community of users.
**Heroku** for hosting. Django/Python is one of the main infrastructures/languages that it supports.
**SQLite** for development server. Queries are very fast and appropriate for development.
**PostgreSQL** for production server. This is provided for free by Heroku.

###Models

####FoodTrucks
This model represents the food trucks. It will have the most important data as its fields:
**name** CHAR from *Applicant* field
**address** CHAR from *Address* field
**fooditems** CHAR from *FoodItems* field
**longitude** DECIMAL from *Longitude* field
**latitude** DECIMAL from *Latitude* field
**foodtypes** MANYTOMANY foreign key into FoodTypes objects

####FoodTypes
This model represents the food types. There are 20 items that I pre-determined in FOOD_CHOICES tuple (*tacos, burgers, hot dogs,* etc.):
**food** INTEGER choices


*Relationship*
FoodTrucks and FoodTypes have a many to many relationship. That way, we'll be able to realize the two functionalities I mentioned earlier. Query FoodTrucks on its *longitude* and *latitude*, and we should be able to get a filtered list of food trucks close by with major FoodTypes that it serves. Search for one of the major FoodTypes, and we should be able get all FoodTrucks that serve it.


###Files I Authored
####quickstart/models.py
Holds the FoodTrucks and FoodTypes model. Represents the schema of the database as well.

####quickstart/management/commands/populate.py
Used to populate initial data in the databases using a json-loadable text file. I used DataSF's FoodTrucks endpoint.

*Usage: python manage.py populate datasf.json* 

####quickstart/serializers.py
Determines which FoodTrucks and FoodTypes fields are served when queried. 

####quickstart/tests.py
Unit tests, written to test Views and Models which have custom functions in them.

####quickstart/views.py
Determines the queryset that is returned for FoodTrucks and FoodTypes upon rquest.

FoodTrucksSerializer supports url query parameters to filter FoodTrucks based on longitude, latitude, and distance. For example, if given

*Longitude=-122.394594036205000000000000000000&Latitude=37.787900097818100000000000000000&distance=2*

the results returned will be filtered so that food trucks fall within 2 miles north, south, east, and west. Results are essentially bounded by a square.

####tutorial/urls.py
Binds URI to the views.

###In the future
In the future, I want to implement these functions:
1) Ability to search FoodTrucks for any keywords in the fooditems key
2) Front-end using bootstrap and AngularJS
3) Implement some machine learning to  determine FoodType based off of the fooditems key, rather than using pre-determined FoodTypes.
4) Support filtering FoodTrucks by circular radius instead of box radius.