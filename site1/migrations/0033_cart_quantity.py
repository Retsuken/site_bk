# Generated by Django 4.2 on 2024-08-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0032_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
