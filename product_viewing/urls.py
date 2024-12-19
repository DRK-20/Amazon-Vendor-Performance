from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('results/', views.results, name='results'),
    path('registered/', views.registered_products, name='registered_products'),
]
