# Generated by Django 5.0.6 on 2024-05-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_orderproduct_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
