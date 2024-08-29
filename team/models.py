from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=125)
    positions = models.CharField(max_length=125)
    instagram = models.URLField(max_length=125, null=True, blank=True)
    facebook = models.URLField(max_length=125, null=True, blank=True)
    youtube = models.URLField(max_length=125, null=True, blank=True)
    image = models.ImageField(null=True,blank=True)

    class Meta:
        verbose_name = ('team')
        verbose_name_plural = ('teams')

    def __str__(self) -> str:
        return self.name