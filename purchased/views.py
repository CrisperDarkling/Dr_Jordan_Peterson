from django.shortcuts import render
from products.models import Products


# Create your views here.
def purchased(request):
    products = Products.objects.all()
    return render(request, "purchased.html", {'products': products})