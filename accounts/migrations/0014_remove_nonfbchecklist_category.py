# Generated by Django 3.1.6 on 2021-03-12 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210313_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nonfbchecklist',
            name='category',
        ),
    ]
