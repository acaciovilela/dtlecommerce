from django.shortcuts import render
from dtlcatalog.models import Category

def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})