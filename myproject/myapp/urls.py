# Import necessary functions and modules for defining URL patterns
from django.urls import path
from . import views  # Import views from the same directory as this urls.py file

# Define URL patterns for your app
urlpatterns = [
    # When the root URL is accessed, call the index view function from views.py
    path('', views.index, name='index'),
    
    # When the 'greet/' URL is accessed, call the greet view function from views.py
    path('greet/', views.greet, name='greet'),
]
