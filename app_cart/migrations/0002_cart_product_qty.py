# Generated by Django 3.2 on 2021-05-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_qty',
            field=models.IntegerField(default=1),
        ),
    ]
