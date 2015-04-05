# AUTHOR: Ly Nguyen

from foodtrucks.models import FoodTypes, FoodTrucks
from rest_framework import viewsets, generics
from foodtrucks.serializers import FoodTypesSerializer, FoodTrucksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from LatLon import LatLon

class FoodTypesList(generics.ListAPIView):
    queryset = FoodTypes.objects.all()
    serializer_class = FoodTypesSerializer


class FoodTrucksList(generics.ListAPIView):
    serializer_class = FoodTrucksSerializer

    # Description: Overrides ListAPIView's class method to filter
    #			   on coordinates.
    def get_queryset(self):
    	queryset = FoodTrucks.objects.all()
    	query_long = self.request.QUERY_PARAMS.get('longitude', None)
    	query_lat = self.request.QUERY_PARAMS.get('latitude', None)
    	distance = self.request.QUERY_PARAMS.get('distance', None)

    	if query_long is not None and query_lat is not None:
    		try:
	    		query_long = float(query_long)
	    		query_lat = float(query_lat)
	    	except:
	    		print "Invalid coordinates"
	    		return queryset

	    	try:
    			east_long, west_long, north_last, south_lat = self._get_latlong_range(query_lat, query_long, distance)
    		except:
    			print "Invalid distance"
    			return queryset
    		queryset = queryset.filter(longitude__gt=west_long, longitude__lt=east_long, latitude__gt=south_lat, latitude__lt=north_last)
    	return queryset

    # Description: gets longitudes & latitudes within "distance" miles
    #			   of original coordinates (1 mile by default). Gets
    #			   square, not circular, radius.
    def _get_latlong_range(self, query_lat, query_long, distance):
    	if distance is None:
    		distance = 1
    		print 
    	else:
			try:
				distance = float(distance)
			except:
				print "Cannot convert to number"

    	origin = LatLon(query_lat, query_long)

    	east = origin.offset(90, distance)
    	east_long = float(east.to_string()[1])

    	west = origin.offset(270, distance)
    	west_long = float(west.to_string()[1])

    	north = origin.offset(0, distance)
    	north_last = float(north.to_string()[0])

    	south = origin.offset(180, distance)
    	south_lat = float(south.to_string()[0])

    	return east_long, west_long, north_last, south_lat

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'foodtrucks': reverse('foodtrucks-list', request=request, format=format),
        'foodtypes': reverse('foodtypes-list', request=request, format=format)
    })