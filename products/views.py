from django.shortcuts import render
from .models import Products

# Create your views here.
def all_products(request):
    products = Products.objects.all()
    return render(request, "products2.html", {"products": products})