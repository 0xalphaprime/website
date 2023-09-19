from django.shortcuts import render

# Create your views here.
def zb_dashboard_view(request):
    return render(request, 'zb_dashboard.html')