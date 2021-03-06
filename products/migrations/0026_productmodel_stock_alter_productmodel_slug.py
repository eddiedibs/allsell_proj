# Generated by Django 4.0.3 on 2022-05-18 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_address_orderproduct_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='slug',
            field=models.SlugField(blank=True, default=None, unique=True),
        ),
    ]
