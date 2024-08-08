# Generated by Django 4.2 on 2024-08-03 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0028_alter_product_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site1.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site1.user')),
            ],
        ),
    ]
