from django.db import models


# Create your models here.

class VahiclesModel(models.Model):
    CarId = models.AutoField(primary_key=True)
    year = models.IntegerField()
    carName = models.CharField(max_length=100)
    CarModel = models.CharField(max_length=100)

    def __str__(self):
        return self.carName


class ShopCar(models.Model):
    ShopCarName = models.CharField(max_length=100)
    ShopCarImage = models.ImageField(upload_to='images')
    OffInPercentage = models.IntegerField(default=0)
    CarDetail = models.CharField(max_length=300)

    def __str__(self):
        return self.ShopCarName


class CarParts(models.Model):
    partName = models.CharField(max_length=100)
    partImage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.partName


class Category(models.Model):
    CategoryName = models.CharField(max_length=100)
    CategoryImage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.CategoryName


class TireWheels(models.Model):
    TireWheelsName = models.CharField(max_length=100)
    TireWheelsImage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.TireWheelsName


class Exterior(models.Model):
    ExteriorName = models.CharField(max_length=100)
    ExteriorImage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.ExteriorName


class lighting(models.Model):
    lightingName = models.CharField(max_length=100)
    lightingImage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.lightingName


class BodyPart(models.Model):
    BodyPartName = models.CharField(max_length=100)
    BodyPartImage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.BodyPartName


class Interior(models.Model):
    InteriorName = models.CharField(max_length=100)
    InteriorImage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.InteriorName


class Audio(models.Model):
    AudioName = models.CharField(max_length=100)
    AudioImage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.AudioName


class AutomotiveTools(models.Model):
    AutomotiveToolsName = models.CharField(max_length=100)
    AutomotiveToolsImage = models.ImageField(upload_to='images')

    def __str__(self):
        return self.AutomativeToolsName



