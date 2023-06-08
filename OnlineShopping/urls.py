from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_adminlte.urls')),
    path('', include('shop.urls')),
    path('company/', include('company.urls')),
    path('bidder/', include('bidder.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
