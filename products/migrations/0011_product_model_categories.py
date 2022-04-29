# Generated by Django 4.0.3 on 2022-04-29 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_model_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='categories',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='products.product_category'),
        ),
    ]
