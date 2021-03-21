from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Rectify, Report, NonFBChecklist

class RectifyForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =  '__all__'

class CreateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields =  ['tenant_name', 'issue']
    
    def __init__(self, *args, **kwargs):
        super(CreateReportForm, self).__init__(*args, **kwargs)
        self.fields['issue'].widget = forms.CheckboxSelectMultiple()
        self.fields['issue'].queryset = NonFBChecklist.objects.all()
    

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']