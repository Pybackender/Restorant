from django.contrib import admin

from about.models import About

# Register your models here.
@admin.register(About)
class Aboutadmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image','image2','image3','image4','experience','master_chefs']
    prepopulated_fields = {'slug': ('title',)}


admin.site.site_header = "MR"
admin.site.site_title = "حسن سایت ادمین"
admin.site.index_title = "خوش امدی حسن "