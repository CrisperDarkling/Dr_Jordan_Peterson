from django.shortcuts import render
from products.models import Products
# from blog.models import Post

# Create your views here.

def do_search(request):
    products = Products.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'products2.html', {'Products': products})
    # return render(request, 'products2.html', {'Products': products}, "blogposts.html", {"Post": youtubeposts})