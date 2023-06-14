from django.db import models


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


