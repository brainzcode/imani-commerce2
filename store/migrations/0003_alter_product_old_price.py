# Generated by Django 4.1.5 on 2023-02-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_old_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]