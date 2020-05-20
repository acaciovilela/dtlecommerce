from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'

urlpatterns = [
	path('', views.profile , name="profile"),
	path('register/', views.register , name="register"),
	path('edit/', views.edit , name="edit"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
