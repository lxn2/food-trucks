# AUTHOR: Ly Nguyen
# This command can be used to populate the database
# with a JSON file from DataSF.

from django.core.management.base import BaseCommand, CommandError
from foodtrucks.models import FoodTrucks, FoodTypes
import json
import re

class Command(BaseCommand):
    # command line
    args = '<datasf_file>'
    help = 'Populates models with data, given JSON file'

    # json record column numbers
    columnMeta = {'Applicant': 9, 
                   'Address': 12, 
                   'Status': 18,
                   'FoodItems': 19, 
                   'Latitude': 22, 
                   'Longitude': 23}

    # hold references to foodtype objects
    foodTypeObjs = {}


    # Description: Point of entry. Creates FoodType objects if none exists.
    #              Creates FoodTruck objects in the provided text file.
    def handle(self, *args, **options):
        # create FoodType objects only if none exist
        self._getFoodTypes()

        # open json file
        try:
            fp = open(args[0])
            jsonData = json.load(fp)
        except:
            print 'Cannot read file'
            exit(1)

        # look at food trucks with valid permit status
        for facility in jsonData['data']:
            if facility[self.columnMeta['Status']] == 'APPROVED':

                # pull relevant data
                applicant = facility[self.columnMeta['Applicant']]
                address = facility[self.columnMeta['Address']]
                foodItems = facility[self.columnMeta['FoodItems']]
                latitude = facility[self.columnMeta['Latitude']]
                longitude = facility[self.columnMeta['Longitude']]

                # create FoodTruck objects if truck has a name
                if applicant:
                    foodTruckRecord = FoodTrucks(name=applicant, address=address, 
                        fooditems=foodItems, longitude=longitude, latitude=latitude)
                    foodTruckRecord.save()

                    # add FoodTypes to this FoodTruck if truck had food items listed
                    foundFoodMatch = False
                    if foodItems:
                        foodItems = foodItems.lower() # lowercase

                        # search pre-defined foods in truck's food listing
                        for foodTuple in FoodTypes.FOOD_CHOICES[:-1]: # exclude 'OTHER'
                            foodItem = foodTuple[1]
                            matchObject = re.search(foodItem, foodItems)
                            if (matchObject):
                                foundFoodMatch = True
                                foodTruckRecord.foodtypes.add(self.foodTypeObjs[foodItem])

                    # if no pre-defined foods found in truck's food listing, categorize as 'OTHER'
                    if not foundFoodMatch:
                        foodTruckRecord.foodtypes.add(self.foodTypeObjs['other'])
                print applicant
        fp.close()


    # Description: Gets FoodType objects based on FoodType model's
    #              pre-defined FOOD_CHOICES tuple 
    def _getFoodTypes(self):
        # create FoodType objects only if none exist
        if len(FoodTypes.objects.all()) == 0:
            for foodTuple in FoodTypes.FOOD_CHOICES:
                foodTypeNum = foodTuple[0]
                foodTypeStr = foodTuple[1]
                self.foodTypeObjs[foodTypeStr] = FoodTypes(food=foodTypeNum)
                self.foodTypeObjs[foodTypeStr].save()
        # if they exist, reference them
        else:
            for foodTuple in FoodTypes.FOOD_CHOICES:
                foodTypeNum = foodTuple[0]
                foodTypeStr = foodTuple[1]
                self.foodTypeObjs[foodTypeStr] = FoodTypes.objects.filter(food=foodTypeNum)[0]

