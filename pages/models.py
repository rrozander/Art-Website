from email.mime import image
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length=50)
