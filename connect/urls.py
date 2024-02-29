from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('private_policy/', views.private_policy, name='private_policy'),
]
