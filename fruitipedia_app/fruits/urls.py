
from django.contrib import admin
from django.urls import path, include

from fruitipedia_app.fruits.views import Homepage, Dashboard, AddFruit, DetailsFruit, EditFruit, DeleteFruit

urlpatterns = [
    path('create/', AddFruit.as_view(), name='add fruit'),
    path('<int:pk>/details/', DetailsFruit.as_view(), name='details fruit'),
    path('<int:pk>/edit/', EditFruit.as_view(), name='edit fruit'),
    path('<int:pk>/delete/', DeleteFruit.as_view(), name='delete fruit'),

]
