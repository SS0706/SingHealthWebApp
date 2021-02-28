from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q
# Create your views here.

def home(request):
    orders = Order.objects.all()
    stores = Store.objects.all()
    
    total_orders = orders.count()
    pending = orders.filter(Q(status='Pending')|Q(status='Notification Sent')).count()
    
    context = {'orders':orders, 'stores':stores, 'pending':pending}
    return render(request, 'accounts/dashboard.html', context)
def stores(request):
    stores = Store.objects.all()
    
    return render(request, 'accounts/stores.html', {'stores':stores})
def report(request):
    return render(request, 'accounts/report.html')
def announcements(request):
    return render(request, 'accounts/announcements.html')
