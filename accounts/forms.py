from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order, Report, NonFBChecklist, CovidComplianceChecklist, FBChecklist


class RectifyForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget = forms.Textarea)

class CreateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['store', 'report_number', 'compliance']

    def __init__(self, *args, **kwargs):
        super(CreateReportForm, self).__init__(*args, **kwargs)
        self.fields['compliance'].widget = forms.CheckboxSelectMultiple()
        self.fields['compliance'].queryset = NonFBChecklist.objects.all()


class CreateUserForm(UserCreationForm):
    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()

        username = cleaned_data.get('username')
        if username and User.objects.filter(username__iexact=username).exists():
            self.add_error(
                'username', 'A user with that username already exists.')

        email = cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            self.add_error(
                'email', 'A user with that email already exists.')

        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
