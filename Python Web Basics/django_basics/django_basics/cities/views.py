from django.shortcuts import render

from django_basics.cities.models import Person


def index(req):
    context = {
        'name': 'Assia',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)
