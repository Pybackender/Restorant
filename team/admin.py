from django.contrib import admin

from team.models import Team

@admin.register(Team)
class reservationadmin(admin.ModelAdmin):
    list_display = ['name','positions','image','instagram','facebook','youtube']