from django.shortcuts import render
from . import cart

def show(request):
    if request.method == 'POST':
        data = request.POST
        if data['submit'] == 'Remove':
            cart.remove_from_cart(request)
        if data['submit'] == 'Update':
            cart.update_cart(request)
    cart_items = cart.get_cart_items(request)
    cart_subtotal = cart.cart_subtotal(request)
    return render(request, 'show.html', {'cart_items': cart_items, 'cart_subtotal': cart_subtotal})
