# Generated by Django 4.2 on 2024-08-06 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0041_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
