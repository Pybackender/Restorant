from django.http import HttpResponseRedirect
from django.shortcuts import render
from about.models import About
from account.forms import ReservationForm
from account.models import User
from contact.models import Contact
from reservation.models import Reservation
from services.models import service
from menu.models import Category, Menu
from team.models import Team
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import get_user_model

from testimonial.models import Testimonial

User = get_user_model()


def accountView(request):
    user = User.objects.all()
    about = About.objects.all()
    services = service.objects.all()
    menu = Menu.objects.all()
    menu2 = Category.objects.all()
    team = Team.objects.all()
    contact = Contact.objects.all()
    reservation = Reservation.objects.all()
    testimonial = Testimonial.objects.all()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():

            form.save()
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            email = form.cleaned_data["email"]
            datetime = form.cleaned_data["datetime"]
            no_of_people = form.cleaned_data["no_of_people"]
            special_request = form.cleaned_data["special_request"]
            recipients = ["backender.py@gmail.com"]

            try:
                send_mail(
                    subject=name,  # Subject can be the name or a custom subject
                    message=f"Message: {message}\nno_of_people: {no_of_people}\nFrom: {email}",
                    from_email=email,
                    recipient_list=recipients,
                )
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")

            
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return HttpResponseRedirect("contact.html#")

    else:
        form = ReservationForm()

    return render(request, 'landing/index.html', context={
        'user': user,
        'about': about,
        'services': services,
        'menu': menu,
        'menu2': menu2,
        'form': form,
        'reservation': reservation,
        'team': team,
        'contact': contact,
        'testimonial': testimonial,
    })
