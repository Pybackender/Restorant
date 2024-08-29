from django.db import models

class service(models.Model):
    title = models.CharField(max_length=125,null=True,blank=True)
    slug = models.CharField(max_length=125,null=True,blank=True)
    content = models.CharField(max_length=300,null=True,blank=True)
    icon = models.CharField(max_length=128, blank = True, null = True)

    class Meta:
        verbose_name = ('service')
        verbose_name_plural = ('services')

    def __str__(self) -> str:
        return self.title