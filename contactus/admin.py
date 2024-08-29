from django.contrib import admin

from contactus.models import Contactus, Emails

# Register your models here.
@admin.register(Contactus)
class reservationadmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_email','customer_name','customer_subject','message']

@admin.register(Emails)
class reservationadmin(admin.ModelAdmin):
    list_display = ['name','email']