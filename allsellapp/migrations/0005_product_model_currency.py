# Generated by Django 4.0.3 on 2022-03-14 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allsellapp', '0004_product_model_prod_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='currency',
            field=models.CharField(choices=[('$', 'US Dollars ($)')], default='$', max_length=5),
        ),
    ]
