from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap/', include('home.urls')),
    path('', include('home.urls')),
    path('book/', include('book.urls')),
    path('home/', include('home.urls')),
    path('catalog/', include('catalog.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
