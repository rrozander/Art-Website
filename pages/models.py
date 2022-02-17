from email.mime import image
from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length=50, unique=True)

  def get_absolute_url(self):
      return reverse("category", kwargs={"pk": self.pk})

class About(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  instagram_username = models.CharField(max_length=50)