# Generated by Django 3.1.6 on 2021-03-10 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_nonfbchecklist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='name',
            new_name='reportID',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='phone',
            new_name='tenantName',
        ),
    ]
