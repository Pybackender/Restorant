from django.db import models

class About(models.Model):
    title = models.CharField(max_length=125)
    slug = models.CharField(max_length=125)
    content = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    image2 = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    image3 = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    image4 = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    experience =models.IntegerField(null=True,blank=True)
    master_chefs =models.IntegerField(null=True,blank=True)

    class Meta:
        verbose_name = ('about')
        verbose_name_plural = ('abouts')

    def __str__(self):
        return self.title 
