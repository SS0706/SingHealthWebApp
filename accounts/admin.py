from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Report)
admin.site.register(Store)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(NonFBChecklist)

