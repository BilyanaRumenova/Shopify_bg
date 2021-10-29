from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shopify_bg.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('store/', include('shopify_bg.store.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
