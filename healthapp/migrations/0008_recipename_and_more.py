# Generated by Django 4.2.1 on 2023-06-26 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0007_weightloss_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeName',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('mzr_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='product',
            new_name='product_name',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='title',
        ),
        migrations.RemoveField(
            model_name='recipecategoryname',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='cooking_condition',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='healthapp.cookingcondition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='size_name_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='healthapp.sizename'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='RecipeNutrient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.FloatField()),
                ('nutrient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthapp.nutrientname')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthapp.recipe')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthapp.unit')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='healthapp.recipename'),
            preserve_default=False,
        ),
    ]
