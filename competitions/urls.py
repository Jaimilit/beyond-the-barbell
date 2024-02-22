from django.urls import path
from . import views

urlpatterns = [
    path('competitions/', views.competitions, name='competitions'),
    path('book_competition/<int:competition_id>/', views.booking, name='book_competition'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('booking/', views.booking, name='booking'),
    path('book_competition/<int:competition_id>/', views.booking, name='book_competition'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),

]