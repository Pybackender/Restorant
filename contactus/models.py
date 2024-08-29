from django.db import models

# Create your models here.
class Emails(models.Model):
    name =models.CharField(max_length=125,null=True,blank=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'


    def __str__(self):
        return self.name
    

class Contactus(models.Model): 
    customer_name =models.CharField(max_length=125,null=True,blank=True)
    customer_email = models.EmailField(null=True, blank=True)
    customer_subject =models.CharField(max_length=125,null=True,blank=True)
    message =models.CharField(max_length=225,null=True,blank=True)

    class Meta:
        verbose_name = 'contactus'
        verbose_name_plural = 'contactsus'


    def __str__(self):
        return self.customer_name
    

       