from django.contrib import admin
from django.urls import path, include   # ✅ import include once

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # ✅ connect to app-level urls
]
