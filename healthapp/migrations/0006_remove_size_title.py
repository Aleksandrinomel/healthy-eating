# Generated by Django 4.2.1 on 2023-06-26 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0005_alter_product_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='title',
        ),
    ]
