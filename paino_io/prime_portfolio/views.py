from django.shortcuts import render

# Create your views here.
def prime_portfolio_view(request):
    return render(request, 'prime_portfolio.html')