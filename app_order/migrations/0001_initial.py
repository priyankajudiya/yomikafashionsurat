# Generated by Django 3.2 on 2021-05-30 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_products', '0007_auto_20210530_1759'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderCreatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.CharField(max_length=1000)),
                ('qty', models.IntegerField()),
                ('size', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending', max_length=15)),
                ('product_sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
