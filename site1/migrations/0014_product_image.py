# Generated by Django 4.2 on 2024-02-25 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0013_alter_product_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='products_images'),
            preserve_default=False,
        ),
    ]
