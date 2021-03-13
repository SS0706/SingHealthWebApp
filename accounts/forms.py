from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order
from .models import Report

class RectifyForm(ModelForm):
    class Meta:
        model = Order
        fields =  '__all__'

class CreateReportForm(ModelForm):
    class Meta:
        model = Report
        fields =  ['tenant_name', 'issue']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']