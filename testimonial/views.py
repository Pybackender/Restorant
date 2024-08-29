from django.shortcuts import render

from contact.models import Contact
from testimonial.models import Testimonial

# Create your views here.
def TestimonialView(request):
    contact = Contact.objects.all()
    testimonial = Testimonial.objects.all()


    return render(request, 'landing/testimonial.html', context={

        'testimonial': testimonial,
        'contact': contact,

    })

