from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=125)
    slug = models.CharField(max_length=125)
    content = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    position = models.CharField(max_length=125, null=True, blank=True)

    class Meta:
        verbose_name = ('Testimonial')
        verbose_name_plural = ('Testimonials')

    def __str__(self):
        return self.name 
