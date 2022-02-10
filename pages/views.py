from django.shortcuts import get_object_or_404, render

from .models import Category

# Create your views here.
def home_view(requests):
  return render(requests, 'home.html', {})

def about_view(requests):
  return render(requests, 'about.html', {})

def category_view(request, category_name):
  category_obj = get_object_or_404(Category, category_name=category_name)
  context = {
    'category': category_obj
  }
  return render(request, 'category_page.html', context)