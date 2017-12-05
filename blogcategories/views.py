from django.shortcuts import render
from .models import YoutubeCategory

# Create your views here.
def youtube_categories(request):
    youtubecategories = YoutubeCategory.objects.all()
    return render(request, "youtubecategories.html", {"youtubecategories": youtubecategories})
    
    
