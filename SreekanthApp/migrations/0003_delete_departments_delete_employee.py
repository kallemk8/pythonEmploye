# Generated by Django 4.1.6 on 2023-02-07 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SreekanthApp', '0002_departments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Departments',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
