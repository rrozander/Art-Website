from django.db import models

from pages.models import Category
# Create your models here.

class Art(models.Model):
  title = models.CharField(max_length=50)
  creation_date = models.DateField()
  homepage = models.BooleanField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
      return self.title

class ArtImage(models.Model):
  image = models.ImageField(upload_to='art_images/')
  art_project = models.ForeignKey(Art, on_delete=models.CASCADE)