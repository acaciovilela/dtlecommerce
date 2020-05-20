from django.shortcuts import render
from dtlcatalog.models import Category

def index(request):
    return render(request, 'index.html', {})
