from django.contrib import admin

from reservation.models import Reservation

# Register your models here.
@admin.register(Reservation)
class Reservationadmin(admin.ModelAdmin):
    list_display = ['name','email','datetime','no_of_people','special_request']
