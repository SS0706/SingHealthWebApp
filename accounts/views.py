from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, EmailMessage
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
    print(reports)
    # TODO: fix total_score
    #total_score = reports.compliance.all()
    total_score = 0
    print(total_score)

    context = {'reports': reports, 'total_score': total_score}
    return render(request, 'accounts/reports.html', context)


def statistics_page(request):
    statistics_page = Statistics_page.objects.all()
    return render(request, 'accounts/statistics_page.html', {'statistics_page': statistics_page})


def announcements(request):
    announcements = Announcement.objects.all()
    return render(request, 'accounts/announcements.html', {'announcements': announcements})


@user_passes_test(lambda u: u.is_superuser)
def send_email(request):
    # if request.method == 'GET':
    message = request.POST.get('message', '')
    subject = request.POST.get('subject', '')
    mail_id = request.POST.get('email', '')
    email = EmailMessage(subject, message, 'esc.sutd@gmail.com', [mail_id])
    email.content_subtype = 'html'
    # file=open("README.md", "r")
    # email.attach("README.md", file.read(), 'text/plain')
    # file_upload =request.FILES['file']
    # email.attach(filename, file_upload.read(), file_upload.content_type)
    # email.send()
    # HttpResponse("Sent")
    return render(request, 'accounts/send_email.html', {'send_email': send_email})


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username').lower()
            email = form.cleaned_data.get('email').lower()

            group = Group.objects.get(name='admin')
            user.groups.add(group)

            brk = True

            try:
                User.objects.get(username__iexact=username)
            except:
                brk = False

            if brk:
                messages.warning(request, 'Username already in use')
                return redirect('login')

            user = form.save()
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
    if request.method == 'POST':
        form = RectifyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RectifyForm()
    context = {'form': form}
    return render(request, 'accounts/rectify_form.html', context)


def createReport(request):
    if request.method == 'POST':

        form = CreateReportForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            # instance.save()
            form.save()
            return redirect('/')

    else:
        form = CreateReportForm()
    context = {'form': form}
    return render(request, 'accounts/createReport_form.html', context)
