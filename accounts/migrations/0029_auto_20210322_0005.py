# Generated by Django 3.1.6 on 2021-03-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_covidchecklist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CovidChecklist',
            new_name='CovidComplianceChecklist',
        ),
        migrations.CreateModel(
            name='FBChecklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('tags', models.ManyToManyField(blank=True, to='accounts.Tag')),
            ],
        ),
    ]
