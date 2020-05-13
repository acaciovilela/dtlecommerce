from django.urls import path

from . import views

app_name = 'dtlauth'

urlpatterns = [
    path('', views.index, name='index')
]
