from django.db import models

from pages.models import Category
# Create your models here.

class Project(models.Model):
  title = models.CharField(max_length=50)
  creation_date = models.DateField()
  homepage = models.BooleanField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
      return self.title

class ArtImage(models.Model):
  image = models.ImageField(upload_to='art_images/', default='default/error image.png')
  project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)

  # Will delete project if you delete the last image. 
  def delete(self, using=None, keep_parents=False):
    self.image.delete()
    super().delete()
    if self.project.images.first() is None:
      self.project.delete()

  def __str__(self):
    return self.project.title