# Generated by Django 2.2.23 on 2021-09-23 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture_color', '0003_auto_20210923_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='colour',
            new_name='color',
        ),
    ]
