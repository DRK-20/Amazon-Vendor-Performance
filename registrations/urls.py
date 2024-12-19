from django.urls import path
from . import views

app_name = 'registrations'

urlpatterns = [
    path('register/', views.register_product, name='register_product'),
    path('delete/<int:pk>/', views.delete_registered_product, name='delete_registered_product'),
]
