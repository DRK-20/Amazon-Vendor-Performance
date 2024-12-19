from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from registrations.models import RegisteredProduct
from .models import Analysis
from .genai_script import get_genai_response
from .utils import parse_genai_response

@login_required
def analyze_product(request):
    if request.method == 'POST':
        asin = request.POST.get('asin')
        product = get_object_or_404(RegisteredProduct, asin=asin, user=request.user)

        response_text = get_genai_response({
            'product_name': product.product_name,
        })

        analysis_data = parse_genai_response(response_text)

        analysis = Analysis.objects.create(
            product=product,
            issues=analysis_data.get('issues', []),
            suggestions=analysis_data.get('suggestions', [])
        )

        messages.success(request, "Product analysis completed successfully!")
        return redirect('analysis_results', product_id=product.id)

    return render(request, 'analysis_genai/analyze_product.html') 

@login_required
def analysis_results(request, product_id):
    product = get_object_or_404(RegisteredProduct, id=product_id, user=request.user)
    analyses = product.analyses.all()

    context = {
        'product': product,
        'analyses': analyses,
    }
    return render(request, 'analysis_genai/analysis_results.html', context)
