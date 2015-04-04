# AUTHOR: Ly Nguyen

from django.test import TestCase
from foodtrucks.models import FoodTypes, FoodTrucks
from foodtrucks.views import FoodTrucksList
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.test import Client
from LatLon import LatLon

class ModelsTest(TestCase):
	"""Test Models"""

	def test_foodtype_model(self):
		"""Test FoodType get_FIELD_display() (human-readable string)"""
		a = FoodTypes.objects.create(food=0)
		self.assertTrue(isinstance(a, FoodTypes))
		self.assertEqual(a.get_food_display(), 0)

	def test_foodtype_model2(self):
		"""Test FoodType get_FIELD_display() (human-readable string)"""
		vietnamese = FoodTypes.objects.create(food=6)
		self.assertTrue(isinstance(vietnamese, FoodTypes))
		self.assertEqual(vietnamese.get_food_display(), 'vietnamese')

	def test_foodtype_model3(self):
		"""Test FoodType __unicode__()"""
		a = FoodTypes.objects.create(food=3)
		self.assertTrue(isinstance(a, FoodTypes))
		self.assertEqual(a.__unicode__(), str(a.id) + ": " + FoodTypes.FOOD_CHOICES[a.food-1][1])

	def test_foodtruck_model(self):
		"""Test FoodTrucks __unicode__()"""
		a = FoodTrucks.objects.create(name="name", address="9999 bellevue", 
                        fooditems="this, that, those", 
                        longitude=-122.393472931800000000000000000000, 
                        latitude=37.786091463425100000000000000000)
		self.assertTrue(isinstance(a, FoodTrucks))
		self.assertEqual(a.__unicode__(), str(a.id) + ": " + a.name)

class ViewsTest(APITestCase):
	"""Test Views"""

	def test_foodtype_view(self):
		"""Test URL resource"""
		w = FoodTypes.objects.create(food=2)
		url = reverse("foodtypes-list")
		resp = self.client.get(url)

		self.assertEqual(resp.status_code, 200)
		self.assertIn(w.get_food_display(), resp.content)

	def test_foodtruck_view(self):
		"""Test _get_latlong_range() and get_queryset()"""
		foodtruckslist = FoodTrucksList()
		c = Client()

		w = FoodTrucks.objects.create(name="name", address="9999 bellevue", 
                        fooditems="this, that, those", 
                        longitude=-122.396536309753000000000000000000, 
                        latitude=37.784979887073500000000000000000)
		v = FoodTrucks.objects.create(name="name", address="9999 bellevue", 
                        fooditems="this, that, those", 
                        longitude=-122.398235074249000000000000000000, 
                        latitude=37.786319798284000000000000000000)
		east_long, west_long, north_last, south_lat = \
			FoodTrucksList._get_latlong_range(foodtruckslist, w.latitude, w.longitude, 1)
		origin = LatLon(w.latitude, w.longitude)
		east = LatLon(w.latitude, east_long)

		response = c.get('/foodtrucks/', {'longitude': w.longitude, 'latitude': w.latitude})
		filtered = FoodTrucks.objects.all().filter(longitude__gt=west_long, 
			longitude__lt=east_long, latitude__gt=south_lat, latitude__lt=north_last)

		self.assertTrue(abs(origin.distance(east) - 1) < 0.00001)
		self.assertEqual(len(filtered), len(response.data['results']))
