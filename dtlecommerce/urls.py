from django.contrib import admin
from django.urls import path, include
from .views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('user/', include('dtluser.urls')),
    path('catalog/', include('dtlcatalog.urls')),
    path('cart/', include('dtlcart.urls')),
    path('order/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
