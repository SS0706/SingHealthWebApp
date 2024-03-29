# Generated by Django 3.1.7 on 2021-04-08 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_auto_20210409_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_number', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('compliance', models.ManyToManyField(to='accounts.CovidComplianceChecklist')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.store')),
            ],
        ),
    ]
