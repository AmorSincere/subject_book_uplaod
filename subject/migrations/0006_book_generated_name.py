# Generated by Django 3.2.9 on 2021-11-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0005_course_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='generated_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
