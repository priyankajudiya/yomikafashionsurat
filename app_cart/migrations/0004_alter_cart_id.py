# Generated by Django 3.2 on 2021-05-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0003_auto_20210524_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
