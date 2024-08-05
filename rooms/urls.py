from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    # path('home_rooms/', views.home_rooms, name='home_rooms'),
    path('<slug:slug>/', views.room, name='room'),  
]