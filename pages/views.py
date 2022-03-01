from urllib import response
from django.shortcuts import get_object_or_404, render

from .models import Category, About
from art.models import ArtImage
from art.models import Project

# Create your views here.
def home_view(request):
  return render(request, 'home.html', {})


def about_view(requests):
  about_info = get_object_or_404(About)
  context = {
    'about': about_info
  }
  return render(requests, 'about.html', context)


def category_view(request, category_name):
  category_obj = get_object_or_404(Category, category_name=category_name)

  # querylist of art for the displayed art page
  project_list = Project.objects.filter(category=category_obj.id)
  
  # page_art_list = Project.artimage_set.all()
  context = {
    'category': category_obj,
    'project_list' : project_list,
  }
  return render(request, 'category_page.html', context)


# context processor to load objects on every page with navbar
#------------------------------------------------
def category_list(request):
  queryset = Category.objects.all 
  return { 'category_list': queryset }

def insta_username(request):
  about_obj = About.objects.first()
  username_obj = about_obj.instagram_username
  return { 'insta_username':username_obj }
#------------------------------------------------