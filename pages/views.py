from urllib import response
from django.shortcuts import get_object_or_404, render

from .models import Category

# Create your views here.
def home_view(request):
  return render(request, 'home.html', {})

def about_view(requests):
  return render(requests, 'about.html', {})

def category_view(request, category_name):
  category_obj = get_object_or_404(Category, category_name=category_name)
  context = {
    'category': category_obj
  }
  return render(request, 'category_page.html', context)

# context processor to load category list on every page with navbar
def category_list(request):
  queryset = Category.objects.all 
  return { 'category_list': queryset }
  