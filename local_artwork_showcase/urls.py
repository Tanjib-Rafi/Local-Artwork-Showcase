from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('artworks.urls')),
    path('user/', include('accounts.urls')),
    
]