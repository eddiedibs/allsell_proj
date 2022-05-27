# Generated by Django 4.0.3 on 2022-05-27 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_colourvariation_orderitem_sizevariation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='available_colours',
            field=models.ManyToManyField(to='products.colourvariation'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='available_sizes',
            field=models.ManyToManyField(to='products.sizevariation'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
