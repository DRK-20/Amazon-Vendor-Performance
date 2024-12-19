from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze_product, name='analyze_product'),
    path('results/<int:product_id>/', views.analysis_results, name='analysis_results'),
]
