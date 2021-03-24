from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# Register your models here.
from django.http import HttpResponse, HttpResponseForbidden
from .actions import export_as_csv_action
from .models import *

class RectifyAdmin(admin.ModelAdmin):
    list_display = ['store', 'report', 'date_created']
    actions = [export_as_csv_action("CSV Export", fields=['wink','nudge'])]

admin.site.register(Report)
admin.site.register(Store)
admin.site.register(Tag)
admin.site.register(Order, RectifyAdmin)
admin.site.register(NonFBChecklist)
admin.site.register(Announcement)
admin.site.register(CovidComplianceChecklist)
admin.site.register(FBChecklist)
