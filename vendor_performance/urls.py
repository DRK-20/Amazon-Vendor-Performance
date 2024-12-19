from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('registrations/', include('registrations.urls', namespace='registrations')),
    path('products/', include('product_viewing.urls', namespace='products')),
    path('analysis/', include('analysis_genai.urls')),
    path('scraper/', include('scraper.urls')),
    path('', include('landing.urls', namespace='landing')),
]
