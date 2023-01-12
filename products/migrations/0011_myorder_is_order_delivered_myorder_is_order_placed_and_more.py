# Generated by Django 4.1.4 on 2022-12-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_myorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='is_order_delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myorder',
            name='is_order_placed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myorder',
            name='is_order_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myorder',
            name='order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
