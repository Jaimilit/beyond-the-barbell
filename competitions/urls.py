from django.urls import path
from . import views

urlpatterns = [
    path('competitions/', views.competitions, name='competitions'),
]