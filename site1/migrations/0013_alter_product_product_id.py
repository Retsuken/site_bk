# Generated by Django 4.2 on 2024-02-25 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0012_remove_product_image_remove_product_product_addr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.TextField(unique=True),
        ),
    ]
