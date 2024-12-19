from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from registrations.models import RegisteredProduct
from scraper.scraper_script import get_product_details

@login_required
def dashboard(request):
    return render(request, 'product_viewing/dashboard.html')

@login_required
def results(request):
    asin = request.GET.get('asin')
    product_data = get_product_details(asin)

    context = {
        'product_name': product_data.get('product_name', 'Not Available'),
        'average_rating': product_data.get('average_rating', 'Not Available'),
        'rating_breakdown': product_data.get('rating_breakdown', []),
    }
    return render(request, 'product_viewing/results.html', context)

@login_required
def registered_products(request):
    products = RegisteredProduct.objects.filter(user=request.user)
    return render(request, 'product_viewing/registered_products.html', {'products': products})
