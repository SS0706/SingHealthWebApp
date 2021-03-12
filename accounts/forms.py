from django.forms import ModelForm
from .models import Order
from .models import Report

class RectifyForm(ModelForm):
    class Meta:
        model = Order
        fields =  '__all__'

class CreateReportForm(ModelForm):
    class Meta:
        model = Report
        fields =  '__all__'