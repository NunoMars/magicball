from django.contrib import admin
from django.urls import path
from ball8 import index
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", index, name="home"),
    path("admin", admin.site.urls, name="admin"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

