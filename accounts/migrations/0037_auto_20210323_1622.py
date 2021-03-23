# Generated by Django 3.1.7 on 2021-03-23 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20210323_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='email',
        ),
        migrations.RemoveField(
            model_name='report',
            name='phone',
        ),
        migrations.AddField(
            model_name='store',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
