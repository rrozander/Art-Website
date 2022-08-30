from email.mime import image
from unicodedata import category
from django.db import models
from django.forms import ValidationError
from django.urls import reverse

# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length=50, unique=True)

  def get_absolute_url(self):
      return reverse("category", kwargs={"pk": self.pk})

  def __str__(self):
    return self.category_name

class About(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  description = models.TextField()
  instagram_username = models.CharField(max_length=50)
  photo = models.ImageField(upload_to='about/', default='default/error image.png')

  def save(self, *args, **kwargs):
    return super(About, self).save(*args, **kwargs)

  def clean(self, *args, **kwargs):
    if not self.pk and About.objects.exists():
      raise ValidationError('There can only be one about instance')
  
  def __str__(self):
    return self.name