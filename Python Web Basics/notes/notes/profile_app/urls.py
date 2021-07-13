from django.urls import path

from notes.profile_app.views import profile_page, delete_profile, create_profile

urlpatterns = [
    path('', profile_page, name='profile page'),
    path('create/', create_profile, name='create_profile'),
    path('delete/', delete_profile, name='delete profile')
]
