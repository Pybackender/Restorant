from django import forms
from reservation.models import Reservation

class ReservationForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # datetime = forms.DateTimeField()
    # no_of_people = forms.ChoiceField(choices=[(1, 'People 1'), (2, 'People 2'), (3, 'People 3')])
    # special_request = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Reservation  # Specify the model
        fields = ['name', 'email', 'datetime', 'no_of_people', 'special_request']
