# Generated by Django 4.2.1 on 2023-06-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0006_remove_size_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='weightloss',
            name='quantity',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]
