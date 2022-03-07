from django.shortcuts import get_object_or_404, render

from .models import Project

# Create your views here.
def art_carousel_view(request, category_name, title):
  project = get_object_or_404(Project, title=title)
  # allows for first image in image set to be active in carousel
  first_image = project.images.first()
  other_images = project.images.exclude(pk=first_image.pk)

  count_list = range(1, other_images.count()+1)
  context = {
    'project': project,
    'first_image': first_image,
    'other_images': other_images,
    'count_list': count_list,
  }
  return render(request, 'art_carousel.html', context)