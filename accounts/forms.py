from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order, Report, NonFBChecklist, CovidComplianceChecklist, FBChecklist

class RectifyForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =  '__all__'
        #file = forms.FileField()

class CreateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields =  ['store', 'report_number','issue']
        
    
    def __init__(self, *args, **kwargs):
        super(CreateReportForm, self).__init__(*args, **kwargs)
        self.fields['issue'].widget = forms.CheckboxSelectMultiple()
        self.fields['issue'].queryset = NonFBChecklist.objects.all()
    

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']