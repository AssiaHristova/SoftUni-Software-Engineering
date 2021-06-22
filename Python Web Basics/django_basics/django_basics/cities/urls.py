#cities.urls
from django.urls import path
from django.views.generic import TemplateView
from django_basics.cities.views import index, list_phones

urlpatterns = [
    path('', index), # /cities/
    path('phones/', list_phones), # /cities/ + /phones/ = /cities/phones/
    path('phones2/', TemplateView.as_view(template_name='phones.html')),
]
