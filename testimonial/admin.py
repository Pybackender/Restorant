from django.contrib import admin

from testimonial.models import Testimonial

# Register your models here.
@admin.register(Testimonial)
class Aboutadmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'image','position']
    prepopulated_fields = {'slug': ('name',)}