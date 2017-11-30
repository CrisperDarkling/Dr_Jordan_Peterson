from django.shortcuts import render, redirect, reverse, get_object_or_404

def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart2.html")
    
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart    
    return redirect(reverse('view_cart'))
    


def adjust_cart(request, id):
    """Adjust the quantity of the spefied product to the specified amount"""
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart    
    return redirect(reverse('view_cart'))
