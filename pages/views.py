from django.shortcuts import render

# Create your views here.
def home_view(requests):
  return render(requests, 'home.html', {})

def about_view(requests):
  return render(requests, 'about.html', {})