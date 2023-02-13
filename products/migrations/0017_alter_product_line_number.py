# Generated by Django 3.2 on 2023-02-13 13:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_line_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='line_number',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
