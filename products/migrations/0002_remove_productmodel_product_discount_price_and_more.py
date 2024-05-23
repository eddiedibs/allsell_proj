# Generated by Django 5.0.6 on 2024-05-23 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='product_discount_price',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=2, null=True),
        ),
    ]
