# Generated by Django 4.0.3 on 2022-04-29 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_category_product_model_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_model',
            name='categories',
        ),
    ]
