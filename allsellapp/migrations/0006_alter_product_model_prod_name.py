# Generated by Django 4.0.3 on 2022-03-14 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allsellapp', '0005_product_model_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_model',
            name='prod_name',
            field=models.CharField(max_length=40),
        ),
    ]
