from django.db import models

# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length=50)


# class ArtImage(models.Model):

# class Art(models.Model):
#   title = models.CharField()
#   description = models.TextField()
#   creation_date = models.DateField()
#   art_image = 
#   homepage =
#   category = models.ForeignKey(Category, on_delete=models.CASCADE)