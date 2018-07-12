from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('landingpage.urls')),
    path('admin/', admin.site.urls),
]
