from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product, Category
from .forms import ProductAddToCartForm
from cart import cart

def index(request):
    page_title = 'Catálogo de Produtos'
    return render(request, 'catalog/index.html', {'page_title': page_title})

def show_category(request, category_slug):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    return render(request, 'catalog/category.html', {'products': products, 'category': c})

def show_product(request, product_slug):
    p = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        print('Make a post!') #removethis
        form = ProductAddToCartForm(request.POST)
        if form.is_valid():
            print('Form is valid!') #removethis
            cart.add_to_cart(request)
            return redirect('/cart')
    else:
        form = ProductAddToCartForm()
        form.fields['product_slug'].widget.attrs['value'] = product_slug
    return render(request, 'catalog/product.html', {'product': p, 'form': form})
