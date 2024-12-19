from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),  # Landing page
    path('about/', views.about_scraper, name='about_scraper'),
]
