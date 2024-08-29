from django.shortcuts import render

from contact.models import Contact
from menu.models import Category, Menu

# Create your views here.
def menuView(request):
    menu = Menu.objects.all()
    menu2 = Category.objects.all()
    contact = Contact.objects.all()

    return render(request, 'landing/menu.html', context={
        'menu': menu,
        'menu2': menu2,
        'contact': contact,
    })

