from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from contact.models import Contact
from contactus.forms import ContactusForm
from contactus.models import Contactus, Emails
# Create your views here.
def contactusView(request):
    contactus = Contactus.objects.all()
    contactus2 = Emails.objects.all()
    contact = Contact.objects.all()

    if request.method == "POST":
        form = ContactusForm(request.POST)
        if form.is_valid():

            form.save()
            customer_name = form.cleaned_data["customer_name"]
            message = form.cleaned_data["message"]
            customer_email = form.cleaned_data["customer_email"]
            customer_subject = form.cleaned_data["customer_subject"]
            recipients = ["backender.py@gmail.com"]

            try:
                send_mail(
                    subject=customer_name,  # Subject can be the name or a custom subject
                    message=f"Message: {message}\nMobile: {customer_subject}\nFrom: {customer_email}",
                    from_email=customer_email,
                    recipient_list=recipients,
                )
            except Exception as e:
                messages.error(request, f"Error sending email: {e}")

            
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return HttpResponseRedirect("contact.html")

    else:
        form = ContactusForm()

    return render(request, 'landing/contact.html', context={
        'contactus': contactus,
        'contactus2': contactus2,
        'contact': contact,
        'form': form,
    })