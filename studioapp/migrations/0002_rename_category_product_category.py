# Generated by Django 5.0.1 on 2024-01-31 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studioapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='Category',
        ),
    ]
