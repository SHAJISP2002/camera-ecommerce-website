# Generated by Django 5.0.1 on 2024-01-31 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studioapp', '0002_rename_category_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='Catagory',
        ),
    ]
