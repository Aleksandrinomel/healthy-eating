from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=255, null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    kfa = models.FloatField(null=True)
    goal_weight = models.FloatField(null=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    # instance.profile.save()


class UserNeed(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    nutrient_name = models.ForeignKey('NutrientName', on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    product_name = models.ForeignKey('ProductName', on_delete=models.CASCADE, null=True)
    product_category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True)
    source = models.ForeignKey('Source', on_delete=models.CASCADE, null=True)

class ProductName(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    mzr_id = models.IntegerField(null=True)


class ExcludedProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Recipe(models.Model):
    id = models.IntegerField(primary_key=True)
    recipe_name = models.ForeignKey('RecipeName', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    prepare_time = models.IntegerField()
    cook_time = models.IntegerField()
    date = models.DateTimeField()
    intake = models.ForeignKey('Intake', on_delete=models.CASCADE)
    cooking_method = models.ForeignKey('CookingMethod', on_delete=models.CASCADE)
    world_kitchen = models.ForeignKey('WorldKitchen', on_delete=models.CASCADE)
    hot_or_cold = models.CharField(max_length=255)

class RecipeName(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    mzr_id = models.IntegerField(null=True)

class RecipeCategoryName(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    # recipes = models.ManyToManyField(Recipe, through='RecipeCategory')


class RecipeCategory(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_category_name = models.ForeignKey(RecipeCategoryName, on_delete=models.CASCADE)

class Instruction(models.Model):
    id = models.IntegerField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_number = models.IntegerField()
    description = models.CharField(max_length=255)
    imageURL = models.CharField(max_length=255)

class RecipeIngredient(models.Model):
    id = models.IntegerField(primary_key=True)
    size_name_id = models.ForeignKey('SizeName', on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    cooking_condition = models.ForeignKey('CookingCondition', on_delete=models.CASCADE)

class RecipeNutrient(models.Model):
    id = models.IntegerField(primary_key=True)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    nutrient_name = models.ForeignKey('NutrientName', on_delete=models.CASCADE)
    quantity = models.FloatField()

class Unit(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

class WorldKitchen(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

class Intake(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

class CookingMethod(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

class ProductCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

class Source(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

class Size(models.Model):
    id = models.IntegerField(primary_key=True)
    size_name = models.ForeignKey('SizeName', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

class SizeName(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    # sizes = models.ManyToManyField(Size, through='SizeName')

class CookingCondition(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

class WeightLoss(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cooking_condition = models.ForeignKey(CookingCondition, on_delete=models.CASCADE)
    quantity = models.FloatField()

class ProductNutrient(models.Model):
    id = models.IntegerField(primary_key=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    nutrient_name = models.ForeignKey('NutrientName', on_delete=models.CASCADE)
    quantity = models.FloatField()

class CookingLoss(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    nutrient_name = models.ForeignKey('NutrientName', on_delete=models.CASCADE)
    cooking_condition = models.ForeignKey(CookingCondition, on_delete=models.CASCADE)
    quantity = models.FloatField(null=True)

class NutrientName(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

class Food_rus(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    product = models.CharField(max_length=100)
    water = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    ngk = models.FloatField()
    hol = models.FloatField()
    mds = models.FloatField()
    krahmal = models.FloatField()
    carbohydrate = models.FloatField()
    fiber = models.FloatField()
    ok = models.FloatField()
    zola = models.FloatField()
    Na = models.FloatField()
    Ka = models.FloatField()
    Ca = models.FloatField()
    Mg = models.FloatField()
    P = models.FloatField()
    Fe = models.FloatField()
    A1 = models.FloatField()
    b_car = models.FloatField()
    A = models.FloatField()
    E = models.FloatField()
    B1 = models.FloatField()
    B2 = models.FloatField()
    PP1 = models.FloatField()
    PP = models.FloatField()
    C = models.FloatField()
    energy = models.FloatField()

    def __str__(self):
        return self.product


