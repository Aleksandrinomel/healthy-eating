# Generated by Django 4.2.1 on 2023-06-27 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0009_alter_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='healthapp.cookingmethod'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='hot_or_cold',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='intake',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='healthapp.intake'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepare_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='world_kitchen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='healthapp.worldkitchen'),
        ),
    ]
