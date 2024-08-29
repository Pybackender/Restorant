from django.shortcuts import render

from contact.models import Contact
from team.models import Team

# Create your views here.
def teamView(request):
    team = Team.objects.all()
    contact = Contact.objects.all()

    return render(request, 'landing/team.html', context={
        'team': team,
        'contact': contact,
    })