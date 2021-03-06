# Generated by Django 3.2.9 on 2021-11-25 17:14

from django.db import migrations, models
import uploads_app.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_url', models.FileField(upload_to=uploads_app.utils.uploads_url_with_instance)),
                ('original_name', models.CharField(max_length=255)),
                ('generated_name', models.CharField(max_length=255)),
                ('content_type', models.CharField(max_length=400)),
                ('size', models.IntegerField(null=True)),
                ('code', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'uploads',
            },
        ),
    ]
