# Generated by Django 4.1.4 on 2022-12-23 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0013_alter_myorder_product_alter_myorder_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='my_product'),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='my_user'),
        ),
    ]
