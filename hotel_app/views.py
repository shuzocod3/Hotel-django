from django.http import HttpResponse
from django.shortcuts import render, redirect

from hotel_app.models import Room, Booking, Employee

def index(request):
    context = {
        'render_string': 'Hotel Menu'
    }
    return render(request, 'index.html', context)

def room_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'room_list.html', context)

def employee_info(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employee_info.html', context)

def booking_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")
        booking = Booking.objects.create(
            user = request.user,
            room = Room.objects.get(number=room_number),
            start_time = start_time,
            end_time = end_time
        )
        return redirect("booking-details", pk=booking.id)
    else:
        return render(request, template_name="booking_rooms.html")


def booking_details(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
        context = {
            'booking': booking
        }
        return render(request, template_name="booking_details.html", context=context)
    except Booking.DoesNotExist:
        return HttpResponse(
            "This booking doesnt exist",
            status = 404
        )
