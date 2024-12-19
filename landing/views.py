from django.shortcuts import render

def landing_page(request):
    """
    Render the landing page for users who are not logged in.
    """
    return render(request, 'landing/landing_page.html')
