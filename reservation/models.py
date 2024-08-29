from django.db import models
from django.core.validators import validate_email


class Reservation(models.Model):
    name = models.CharField(max_length=125, blank=True)
    email = models.EmailField(validators=[validate_email])
    datetime = models.DateTimeField()
    no_of_people = models.PositiveIntegerField(blank=True) 
    special_request = models.CharField(max_length=225, blank=True)

    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'

    def __str__(self) -> str:
        return self.name if self.name else "Reservation"
