from django.contrib import admin
from .models import VahiclesModel, ShopCar, CarParts, Category, TireWheels, Exterior, lighting, BodyPart, Interior, Audio, AutomotiveTools


# Register your models here.

class VahicleAdmin(admin.ModelAdmin):
    search_fields = ['carName']


admin.site.register(VahiclesModel, VahicleAdmin)


class ShopCarAdmin(admin.ModelAdmin):
    search_fields = ['ShopCarName']


admin.site.register(ShopCar, VahicleAdmin)


class CarPartsAdmin(admin.ModelAdmin):
    search_fields = ['CarPartsName']


admin.site.register(CarParts, CarPartsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['CategoryName']


admin.site.register(Category, CategoryAdmin)


class TireWheelsAdmin(admin.ModelAdmin):
    search_fields = ['TireWheelsName']


admin.site.register(TireWheels, TireWheelsAdmin)


class ExteriorAdmin(admin.ModelAdmin):
    search_fields = ['ExteriorName']


admin.site.register(Exterior, ExteriorAdmin)


class lightingAdmin(admin.ModelAdmin):
    search_fields = ['lightingName']


admin.site.register(lighting, lightingAdmin)


class BodyPartAdmin(admin.ModelAdmin):
    search_fields = ['BodyPartName']


admin.site.register(BodyPart, BodyPartAdmin)


class InteriorAdmin(admin.ModelAdmin):
    search_fields = ['InteriorName']


admin.site.register(Interior, InteriorAdmin)


class AudioAdmin(admin.ModelAdmin):
    search_fields = ['AudioName']


admin.site.register(Audio, AudioAdmin)


class AutomotiveToolsAdmin(admin.ModelAdmin):
    search_fields = ['AutomotiveToolsName']


admin.site.register(AutomotiveTools, AutomotiveToolsAdmin)