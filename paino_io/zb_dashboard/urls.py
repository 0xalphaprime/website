from django.urls import path 
from . import views

# Create your views here.
urlpatterns = [
    path('', views.zb_dashboard_view, name='zb'),
]