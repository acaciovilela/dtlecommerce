from django.shortcuts import render

def home(request):
    return render(request, 'includes/home-page.html', {})
