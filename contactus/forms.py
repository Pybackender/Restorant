from django import forms
from contactus.models import Contactus


class ContactusForm(forms.ModelForm):

    # class ContactForm(forms.Form):
    #     name = forms.CharField(max_length=100)
    #     message = forms.CharField(widget=forms.Textarea)
    #     email= forms.EmailField()
    class Meta:
        model = Contactus
        fields = ['customer_name', 'customer_email', 'customer_subject', 'message']  # List t

