from django.urls import path
from . import views
from .views import sign_in, sign_out, index

urlpatterns = [
    path('', index, name="index"),
    path('create/', views.create, name="create"),
    path('sign-in/', sign_in, name='sign in'),
    path('sign-out', sign_out, name='sign out')
]
