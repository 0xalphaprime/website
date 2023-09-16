from django.urls import path
from .views import NotebookView

urlpatterns = [
    path('', NotebookView.as_view(), name='make_more'),
]
