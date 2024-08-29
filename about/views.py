from django.shortcuts import render

from about.models import About
from contact.models import Contact
from team.models import Team


def aboutView(request):
    about = About.objects.all()
    team = Team.objects.all()
    contact = Contact.objects.all()
    
    return render(request, 'landing/about.html', context={
        'about': about,
        'team': team,
        'contact': contact,
    })
