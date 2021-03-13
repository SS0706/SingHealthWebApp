from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class NonFBChecklist(models.Model):
    checklist_item = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True) # not sure if we actually need this, can remove later

    def __str__(self):
        return self.checklist_item
        
class Store(models.Model):
    CATEGORY = (
        ('Food', 'Food'),
        ('Fashion', 'Fashion')
    )
    #TODO: change the below fields
    name = models.CharField(max_length=200, null=True)
    rectificationNeeded = models.BooleanField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    #to be calculated
    score = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    audit_date = models.DateField("dd/mm/yyyy", auto_now_add=False, null=True)
    tags = models.ManyToManyField(Tag, blank=True) # not sure if we actually need this, can remove later
    
    def __str__(self):
        return self.name

class Report(models.Model):
    tenant_name = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    issue = models.ForeignKey(NonFBChecklist, null=True, on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.tenant_name#give name in the admin panel




#TODO: merge report and order? because order basically extends report Rectify
class Order(models.Model):
    STATUS = (
        ('Notification Sent','Notification Sent'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )
    store = models.ForeignKey(Store, null=True, on_delete=models.SET_NULL)
    report = models.ForeignKey(Report, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    issue = models.ForeignKey(NonFBChecklist, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.report.tenant_name



class Announcement(models.Model):
    announcement_title = models.CharField(max_length=200, null=True)
    announcement_text = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.announcement_title



    
