from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name="index"),
    path('category/<slug:category_slug>/', views.show_category, name="show_category"),
    path('product/<slug:product_slug>/', views.show_product, name="show_product"),
]
