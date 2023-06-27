# Generated by Django 4.2.1 on 2023-06-26 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0002_cookingloss_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductName',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('mzr_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='healthapp.productname'),
            preserve_default=False,
        ),
    ]