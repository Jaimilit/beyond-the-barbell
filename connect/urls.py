from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('private_policy/', views.private_policy, name='private_policy'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('reviews/', views.submit_review, name='reviews'),
]
