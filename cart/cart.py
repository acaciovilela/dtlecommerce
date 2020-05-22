import decimal
import random
from .models import CartItem
from catalog.models import Product
from django.shortcuts import get_object_or_404, redirect

CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY, '') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    print(cart_id) #removethis
    return cart_id

def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_cart_id(request))

def add_to_cart(request):
    data = request.POST
    print(data) #removethis
    product_slug = data.get('product_slug','')
    quantity = data.get('quantity',1)
    p = get_object_or_404(Product, slug=product_slug)
    print(p) #removethis
    cart_products = get_cart_items(request)
    print(p.id) #removethis
    product_in_cart = False
    for cart_item in cart_products:
        print(cart_item.product.id) #removethis
        if cart_item.product.id == p.id:
            cart_item.augment_quantity(quantity)
            print(cart_item.quantity) #removethis
            product_in_cart = True
    if not product_in_cart:
        print('Falhando') #removethis
        ci = CartItem()
        ci.product = p
        ci.quantity = quantity
        ci.cart_id = _cart_id(request)
        ci.save()

def cart_distinct_item_count(request):
    return get_cart_items(request).count()

def get_single_item(request, item_id):
    return get_object_or_404(CartItem, id=item_id, cart_id=_cart_id(request))

def update_cart(request):
    postdata = request.POST
    item_id = postdata['item_id']
    quantity = postdata['quantity']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        if int(quantity) > 0:
                cart_item.quantity = int(quantity)
                cart_item.save()
        else:
            remove_from_cart(request)

def remove_from_cart(request):
    postdata = request.POST
    item_id = postdata['item_id']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        cart_item.delete()

def cart_subtotal(request):
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        cart_total += cart_item.product.price * cart_item.quantity
    return cart_total
