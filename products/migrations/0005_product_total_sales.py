# Generated by Django 4.1.4 on 2022-12-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_sales',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
