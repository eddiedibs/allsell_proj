# Generated by Django 4.0.3 on 2022-04-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_imgs_prod_img_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_imgs',
            name='is_carousel_active',
            field=models.CharField(default='not_active', max_length=10),
            preserve_default=False,
        ),
    ]
