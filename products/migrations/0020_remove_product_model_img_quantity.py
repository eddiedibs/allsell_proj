# Generated by Django 4.0.3 on 2022-05-12 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_remove_banner_imgs_item_banner_imgs_banner_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_model',
            name='img_quantity',
        ),
    ]