# Generated by Django 3.2 on 2023-01-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skin_concern',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
