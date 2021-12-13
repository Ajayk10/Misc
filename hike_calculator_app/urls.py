from django.urls import path
from hike_calculator_app import views


urlpatterns = [
    path('', views.hike, name = 'hike'),
    path('Todo/', views.Todo, name = 'Todo'),
    ]