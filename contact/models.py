from django.db import models

# Create your models here.
class Contact(models.Model):
    address = models.CharField(max_length=50)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    opening_day = models.CharField(max_length=125,null=True, blank=True)
    opening_time= models.CharField(max_length=120,null=True, blank=True)
    Newsletter = models.CharField(max_length=120,null=True, blank=True)
    instagram = models.URLField(max_length=225, null=True, blank=True)
    facebook = models.URLField(max_length=225, null=True, blank=True)
    linkedin = models.URLField(max_length=225, null=True, blank=True)
    youtube = models.URLField(max_length=225, null=True, blank=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


    def __str__(self):
        return self.email
    

