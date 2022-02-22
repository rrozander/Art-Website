from django.db import models

from pages.models import Category
# Create your models here.

class Art(models.Model):
  title = models.CharField(max_length=50)
  creation_date = models.DateField()
  homepage = models.BooleanField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

class ArtImage(models.Model):
  image = models.ImageField()
  art_project = models.ForeignKey(Art, on_delete=models.CASCADE)