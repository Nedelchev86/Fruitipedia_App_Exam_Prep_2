
from django.contrib import admin
from django.urls import path

from fruitipedia_app.fruits.views import Homepage
from fruitipedia_app.profiles.views import CreateProfile, DetailsProfile, EditProfile, DeleteProfile

urlpatterns = [
    path('create/', CreateProfile.as_view(), name="create profile"),
    path('details/', DetailsProfile.as_view(), name="details profile"),
    path('edit/', EditProfile.as_view(), name="edit profile"),
    path('delete/', DeleteProfile.as_view(), name="delete profile"),

]

