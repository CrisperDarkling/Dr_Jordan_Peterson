from django.shortcuts import get_object_or_404
from products.models import Products

def cart_contents(request):
    
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product.count += quantity
        cart_items.append({"id":id, "quantity", quantity, "product", product})
        
    