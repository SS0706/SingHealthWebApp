# Generated by Django 3.1.6 on 2021-03-21 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20210322_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.nonfbchecklist'),
        ),
    ]
