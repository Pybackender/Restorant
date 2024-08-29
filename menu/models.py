from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)
    icon = models.CharField(max_length=125,blank = True, null = True)

    class Meta:
        ordering = ['title']
    indexes = [
        models.Index(fields=['title']),
    ]
    verbose_name = 'category'
    verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Menu(models.Model):
    name = models.SlugField(max_length=50)
    image = models.ImageField(null=True, blank=True,upload_to='myport/%Y/%m/%d')
    price = models.IntegerField(null=True, blank=True)
    content = models.CharField(max_length=225, null=True, blank=True)
    category = models.ForeignKey(Category,
                                 related_name='menus',
                                 on_delete=models.CASCADE)


class Meta:
    ordering = ['-published_at']
    verbose_name = 'menu'
    verbose_name_plural = 'menus'


def __str__(self):
    return self.image
