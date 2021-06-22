# people urls
from django.urls import path

from django_basics.cities.views import index

urlpatterns = [
    path('', index)
]
