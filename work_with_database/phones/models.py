from django.db import models
from PIL import Image
from datetime import *


class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='photo/%y/%m/%d', max_length=50)
    release_date = models.DateField(auto_now_add=True) #format='%Y-%m-%d'
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(allow_unicode='utf-8', db_index=True)

    def __str__(self):
        return self.name



