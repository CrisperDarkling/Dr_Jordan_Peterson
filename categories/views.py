from django.shortcuts import render
from .models import Category

# Create your views here.
def all_categories(request):
    categories = Category.objects.all().order_by('name')
    return render(request, "categories.html", {"categories": categories})