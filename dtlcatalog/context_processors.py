from .models import Category

def catalog(request):
    return {
        'categories': Category.objects.filter(is_active=True),
        'request': request,
    }
