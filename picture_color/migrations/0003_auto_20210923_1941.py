# Generated by Django 2.2.23 on 2021-09-23 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_color', '0002_auto_20210923_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='colour',
            field=models.CharField(max_length=7),
        ),
    ]
