# Generated by Django 4.2 on 2024-08-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0037_alter_orders_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.TextField(),
        ),
    ]
