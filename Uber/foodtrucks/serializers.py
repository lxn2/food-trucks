# AUTHOR: Ly Nguyen

from rest_framework import serializers
from foodtrucks.models import FoodTrucks, FoodTypes

class FoodTypesSerializer(serializers.ModelSerializer):
	food = serializers.CharField(source='get_food_display') # from FoodTypes human-readable field of FOOD_CHOICES
	trucks = serializers.StringRelatedField(many=True) # from FoodTrucks __unicode__
	class Meta:
		model = FoodTypes
		fields = ('food', 'trucks')

class FoodTrucksSerializer(serializers.ModelSerializer):
	foodtypes = serializers.StringRelatedField(many=True) # from FoodTypes __unicode__
	class Meta:
		model = FoodTrucks
		fields = ('name', 'address', 'longitude', 'latitude', 'fooditems', 'foodtypes')