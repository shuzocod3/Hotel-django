from django.urls import path
from hotel_app import views

urlpatterns = [
    path("", views.index, name='index'),
    path('rooms/', views.room_list, name='room_list'),
    path('employees/', views.employee_info, name='employee_info'),
    path('booking_rooms/', views.booking_room, name='booking_room'),
    path('booking-details/<int:pk>', views.booking_details, name='booking-details'),
]