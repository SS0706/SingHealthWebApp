from django.db import models

# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    CATEGORY = (
        ('Food', 'Food'),
        ('Fashion', 'Fashion')
    )
    #TODO: change the below fields
    name = models.CharField(max_length=200, null=True)
    complaint = models.BooleanField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True) # not sure if we actually need this, can remove later
    
    def __str__(self):
        return self.name

#TODO: merge report and order? because order basically extends report
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
    
    def __str__(self):
        return self.report.name
