from django.contrib import admin

# Register your models here.
from .models import  Category,Menu

@admin.register(Menu)
class Portadmin(admin.ModelAdmin):
    list_display = [ 'name','category','image','content','price']
    prepopulated_fields = {'name': ('image',)}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title" , "slug","icon"]
    prepopulated_fields = {'slug': ('title',)}