# Generated by Django 3.2.9 on 2021-11-26 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0003_auto_20211126_2157'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employe',
            table='auth_emp',
        ),
    ]
