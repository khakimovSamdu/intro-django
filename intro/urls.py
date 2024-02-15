from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('grocery/', include('app.urls')),
    path("item/", include('grocery.urls')),
    path('admin/', admin.site.urls)
]