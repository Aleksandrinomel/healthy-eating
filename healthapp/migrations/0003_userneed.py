# Generated by Django 4.2.1 on 2023-06-21 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0002_cookingcondition_cookingmethod_intake_nutrientname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNeed',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.FloatField()),
                ('nutrient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthapp.nutrientname')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthapp.unit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthapp.userinfo')),
            ],
        ),
    ]