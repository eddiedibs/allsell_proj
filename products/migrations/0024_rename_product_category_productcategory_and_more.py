# Generated by Django 4.0.3 on 2022-05-17 10:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0023_delete_banner_imgs_delete_home_banner'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_category',
            new_name='ProductCategory',
        ),
        migrations.RenameModel(
            old_name='Product_img',
            new_name='ProductImg',
        ),
        migrations.RenameModel(
            old_name='Product_model',
            new_name='ProductModel',
        ),
    ]
