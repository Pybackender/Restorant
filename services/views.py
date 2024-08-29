from django.shortcuts import render

from contact.models import Contact
from services.models import service

# Create your views here.
def servicetView(request):
    services = service.objects.all()
    contact = Contact.objects.all()
    return render(request, 'landing/service.html', context={
        'services': services,
        'contact': contact,
    })

