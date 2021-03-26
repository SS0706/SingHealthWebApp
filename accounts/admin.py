from django.contrib import admin
# Register your models here.
from .models import *

class RectifyAdmin(admin.ModelAdmin):
    fields = ['store', 'report', 'status', 'issue', 'covid_compliance']

admin.site.register(Report)
admin.site.register(Store)
admin.site.register(Tag)
admin.site.register(Order, RectifyAdmin)
admin.site.register(NonFBChecklist)
admin.site.register(Announcement)
admin.site.register(CovidComplianceChecklist)
admin.site.register(FBChecklist)
admin.site.register(AuditScore)