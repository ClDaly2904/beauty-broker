# Generated by Django 3.2 on 2023-01-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_skin_concern_friendly_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
