# Generated by Django 4.0.3 on 2022-04-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_imgs_is_carousel_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='img_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
