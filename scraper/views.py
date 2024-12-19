from django.shortcuts import render, redirect

def about(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'scraper/about.html')

def about_scraper(request):
    return render(request, 'scraper/about.html')
