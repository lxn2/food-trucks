# AUTHOR: Ly Nguyen

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from foodtrucks import views

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^foodtypes/$',
        views.FoodTypesList.as_view(),
        name='foodtypes-list'),
    url(r'^foodtrucks/$',
        views.FoodTrucksList.as_view(),
        name='foodtrucks-list')
])