# Generated by Django 3.1 on 2020-08-17 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlemodel',
            old_name='header_image',
            new_name='cover_image',
        ),
    ]