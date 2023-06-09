# Generated by Django 4.2.1 on 2023-06-27 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0012_rename_size_name_id_recipeingredient_size_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('kfa', models.IntegerField(null=True)),
                ('age', models.CharField(max_length=255, null=True)),
                ('sex', models.CharField(max_length=255, null=True)),
                ('quantity', models.FloatField(null=True)),
                ('nutrient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthapp.nutrientname')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthapp.unit')),
            ],
        ),
    ]
