from django.urls import path
from . import views

urlpatterns = [
    path('competitions/', views.competitions, name='competitions'),
    path('book_competition/<int:competition_id>/', views.book_competition, name='book_competition'),
    path('delete_booking/<int:competition_id>/', views.delete_booking, name='delete_booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
]