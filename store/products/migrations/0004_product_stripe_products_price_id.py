# Generated by Django 4.2 on 2023-04-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_options_alter_productcategory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_products_price_id',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
