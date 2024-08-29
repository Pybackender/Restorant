from django.shortcuts import render

from contact.models import Contact
from reservation.models import Reservation

# Create your views here.
def reservationView(request):
    reservation = Reservation.objects.all()
    contact = Contact.objects.all()
    return render(request, 'landing/booking.html', context={
        'reservation': reservation,
        'contact': contact,
    })
