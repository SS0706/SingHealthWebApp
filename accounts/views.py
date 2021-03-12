from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import RectifyForm
from .forms import CreateReportForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
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
    nonfbchecklist = NonFBChecklist.objects.all()
    
    return render(request, 'accounts/report.html', {'nonfbchecklist':nonfbchecklist})

def announcements(request):
    return render(request, 'accounts/announcements.html')

def loginPage(request):
    return render(request, 'accounts/login.html')

#create the form
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/register.html')


def createRectification(request):
    form = RectifyForm()
    if request.method == 'POST':
        #print('Printing POST')
        #post data
        form = RectifyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/rectify_form.html', context)

def createReport(request):
    form = CreateReportForm()
    if request.method == 'POST':
        #print('Printing POST')
        #post data
        form = CreateReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/createReport_form.html', context)