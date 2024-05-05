from rest_framework import serializers
from .models import VahiclesModel, CarParts, Category, TireWheels, Exterior, lighting, BodyPart, Interior, Audio, \
    AutomotiveTools, ShopCar


class VahicleSerializers(serializers.HyperlinkedModelSerializer):
    CarId = serializers.ReadOnlyField()

    class Meta:
        model = VahiclesModel
        fields = "__all__"


class CarPartsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarParts
        fields = '__all__'


class CategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TireWheelsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TireWheels
        fields = "__all__"


class ExteriorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exterior
        fields = "__all__"


class lightingSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lighting
        fields = "__all__"


class BodyPartSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BodyPart
        fields = "__all__"


class InteriorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interior
        fields = "__all__"


class AudioSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"


class AutomotiveToolsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AutomotiveTools
        fields = "__all__"


class ShopCarSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopCar
        fields = "__all__"