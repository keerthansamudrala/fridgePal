from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This is the key line: It includes all the URLs from your core/urls.py file
    path('', include('core.urls')),
]