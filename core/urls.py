from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/balance/', include('apps.balance.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
