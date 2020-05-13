from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.item_list, name="item-list")
]
