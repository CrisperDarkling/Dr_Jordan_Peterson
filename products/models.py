from __future__ import unicode_literals
from categories.models import Category
from django.db import models

class Products(models.Model):
    book_author = models.CharField(max_length=200, default="default")
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, blank=True, default="")
    download_link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name