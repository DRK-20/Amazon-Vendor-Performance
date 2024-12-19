# registrations/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegisterProductForm
from .models import RegisteredProduct
import requests
from bs4 import BeautifulSoup
from .utils import get_page, get_product_name, get_average_rating, get_rating_breakdown
from django.db import IntegrityError, transaction
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

@login_required
def register_product(request):
    if request.method == 'POST':
        form = RegisterProductForm(request.POST)
        if form.is_valid():
            asin = form.cleaned_data['asin']
            url = f"https://www.amazon.in/dp/{asin}"
            page = get_page(url)
            product_name = get_product_name(page)
            
            if not product_name:
                messages.error(request, 'This product doesn\'t exist.')
                logger.warning(f'User {request.user.username} attempted to register unknown ASIN {asin}.')
                return render(request, 'registrations/register_product.html', {'form': form})

            average_rating = get_average_rating(page)
            rating_breakdown = get_rating_breakdown(page)

            try:
                with transaction.atomic():
                    RegisteredProduct.objects.create(
                        user=request.user,
                        asin=asin,
                        product_name=product_name,
                        average_rating=average_rating,
                        rating_breakdown=rating_breakdown,
                    )

                messages.success(request, f'Product "{product_name}" registered successfully!')
                logger.info(f'User {request.user.username} registered ASIN {asin}.')
                return redirect('products:registered_products')
            
            except IntegrityError:
                messages.error(request, 'This product is already registered by another user.')
                logger.warning(f'User {request.user.username} attempted to register existing ASIN {asin}.')
                return render(request, 'registrations/register_product.html', {'form': form})
            
            except Exception as e:
                messages.error(request, f'An unexpected error occurred: {e}')
                logger.error(f'Error registering ASIN {asin} by user {request.user.username}: {e}')
                return render(request, 'registrations/register_product.html', {'form': form})
            
        else:
            messages.error(request, f'This product is already registered by another user.')
            logger.warning(f'Invalid registration attempt by user {request.user.username}: {form.errors}')
            return render(request, 'registrations/register_product.html', {'form': form})
        
    else:
        form = RegisterProductForm()

    return render(request, 'registrations/register_product.html', {'form': form})

@login_required
def registered_products(request):
    products = RegisteredProduct.objects.filter(user=request.user)
    return render(request, 'product_viewing/registered_products.html', {'products': products})

@login_required
def delete_registered_product(request, pk):
    product = get_object_or_404(RegisteredProduct, pk=pk, user=request.user)
    
    if request.method == 'POST':
        product_name = product.product_name
        product.delete()
        messages.success(request, f'Product "{product_name}" has been deleted successfully.')
        logger.info(f'User {request.user.username} deleted RegisteredProduct with ASIN {product.asin}.')
        return redirect('products:registered_products')
    
    context = {
        'product': product
    }
    return render(request, 'registrations/confirm_delete.html', context)


