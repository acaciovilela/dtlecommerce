from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user/', include('dtluser.urls')),
    path('catalog/', include('dtlcatalog.urls')),
    path('order/', include('order.urls')),
]
