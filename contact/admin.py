from django.contrib import admin

from contact.models import Contact

# Register your models here.
@admin.register(Contact)
class reservationadmin(admin.ModelAdmin):
    list_display = ['address','phone','email','instagram','facebook','youtube','linkedin']