from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    stores = Store.objects.all()

    total_orders = orders.count()
    pending = orders.filter(Q(status='Pending') | Q(
        status='Notification Sent')).count()

    context = {'orders': orders, 'stores': stores, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)


def stores(request):
    stores = Store.objects.all()

    return render(request, 'accounts/stores.html', {'stores': stores})


def reports(request):
    reports = Report.objects.all()
    #TODO: fix total_score
    #total_score = reports.filter('compliance').count()
    total_score = 0

    context = {'reports': reports, 'total_score': total_score}
    return render(request, 'accounts/reports.html', context)


def announcements(request):
    announcements = Announcement.objects.all()

    return render(request, 'accounts/announcements.html', {'announcements': announcements})


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def createRectification(request):
    form = RectifyForm()
    if request.method == 'POST':
        #print('Printing POST')
        # post data
        form = RectifyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/rectify_form.html', context)


def createReport(request):
    form = CreateReportForm()
    if request.method == 'POST':
        
        form = CreateReportForm(request.POST)
        
        if form.is_valid():            
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/createReport_form.html', context)
