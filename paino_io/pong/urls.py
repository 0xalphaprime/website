from django.urls import path 
from . import views

# Create your views here.
urlpatterns = [
    path('', views.pong_view, name='pong'),
]