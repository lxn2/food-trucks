# AUTHOR: Ly Nguyen

from django.db import models

# Represents single food items. FoodTypes has many FoodTrucks.
class FoodTypes(models.Model):
	# PYTHON DOESN'T HAVE ANYTHING LIKE ENUM
    BURGER = 1
    HOTDOG = 2
    SANDWICH = 3
    INDIAN = 4
    KOREAN = 5
    VIETNAMESE = 6
    MEXICAN = 7
    CHINESE = 8
    PIZZA = 9
    BBQ = 10
    COLDTRUCK = 11
    TACO = 12
    ITALIAN = 13
    FILIPINO = 14
    SEAFOOD = 15
    ASIAN = 16
    PERUVIAN = 17
    GYRO = 18
    COFFEE = 19
    OTHER = 20
    FOOD_CHOICES = (
        (BURGER, 'burger'),
        (HOTDOG, 'hot dog'),
        (SANDWICH, 'sandwich'),
        (INDIAN, 'indian'),
        (KOREAN, 'korean'),
        (VIETNAMESE, 'vietnamese'),
        (MEXICAN, 'mexican'),
        (CHINESE, 'chinese'),
        (PIZZA, 'pizza'),
        (BBQ, 'bbq'),
        (COLDTRUCK, 'cold truck'),
        (TACO, 'taco'),
        (ITALIAN, 'italian'),
        (FILIPINO, 'filipino'),
        (SEAFOOD, 'seafood'),
        (ASIAN, 'asian'),
        (PERUVIAN, 'peruvian'),
        (GYRO, 'gyro'),
        (COFFEE, 'coffee'),
        (OTHER, 'other'),
    )
    food = models.IntegerField(choices=FOOD_CHOICES,
                                      default=OTHER)

    def __unicode__(self): 
        return str(self.id) + ": " + self.get_food_display()


# Represents food trucks. FoodTrucks has many FoodTypes.
class FoodTrucks(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    fooditems = models.TextField(max_length=600, null=True, blank=True)
    foodtypes = models.ManyToManyField(FoodTypes, null=True, blank=True, related_name='trucks')
    longitude = models.DecimalField(max_digits=50, decimal_places=30, null=True, blank=True)
    latitude = models.DecimalField(max_digits=50, decimal_places=30, null=True, blank=True)

    def __unicode__(self): 
        return str(self.id) + ": " + self.name