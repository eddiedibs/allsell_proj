# Generated by Django 4.0.3 on 2022-05-11 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_home_banner_banner_list_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner_imgs',
            name='item',
        ),
        migrations.AddField(
            model_name='banner_imgs',
            name='banner_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.home_banner'),
        ),
        migrations.AlterField(
            model_name='home_banner',
            name='banner_list_date',
            field=models.CharField(choices=[('January', 'January_banners'), ('February', 'February_banners'), ('March', 'March_banners'), ('May', 'May_banners'), ('June', 'June_banners'), ('July', 'July_banners'), ('August', 'August_banners'), ('September', 'September_banners'), ('November', 'November_banners'), ('December', 'December_banners')], default='Test_period', max_length=30),
        ),
    ]