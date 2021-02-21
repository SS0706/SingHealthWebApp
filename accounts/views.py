from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')
def stores(request):
    stores = Store.objects.all()
    return render(request, 'accounts/stores.html', {'stores':stores})
def report(request):
    return render(request, 'accounts/report.html')
def announcements(request):
    return render(request, 'accounts/announcements.html')
