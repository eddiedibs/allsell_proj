# Generated by Django 4.0.3 on 2022-03-14 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allsellapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='img',
            field=models.ImageField(default='product_default.jpg', upload_to='product_pics'),
        ),
    ]