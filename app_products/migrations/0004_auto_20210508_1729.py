# Generated by Django 3.2 on 2021-05-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0003_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='saller',
            new_name='seller',
        ),
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
    ]