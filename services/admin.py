from django.contrib import admin

from services.models import service

@admin.register(service)
class serviceadmin(admin.ModelAdmin):
    list_display = ['title','content','icon']
    prepopulated_fields = {'slug': ('title',)}
