# Generated by Django 3.2 on 2021-05-08 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0002_rename_weigth_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
    ]