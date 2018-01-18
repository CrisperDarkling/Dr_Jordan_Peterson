from django.shortcuts import render
from .models import Products

# Create your views here.
def all_products(request):
    products = Products.objects.all()
    return render(request, "products2.html", {"products": products})
    
def products_by_category(request, id):
    products = Products.objects.filter(category=id).order_by('book_author')
    return render(request, "products2.html", {"products": products})