# Generated by Django 3.2 on 2023-02-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20230210_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.PositiveBigIntegerField(),
        ),
    ]