from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique = True)
    slug = models.SlugField(max_length=200, unique = True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/tourSpot/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'




class TourSpot(models.Model):
    place = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null = True, blank = True, on_delete = models.SET_NULL)
    
    def __str__(self):
        return self.place

    def get_absolute_urls(self):
        return f'/tourSpot/{self.pk}/'

    




