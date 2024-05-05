from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.shortcuts import render
from .models import VahiclesModel, CarParts, Category, TireWheels, Exterior, lighting, BodyPart, Interior, Audio, AutomotiveTools, ShopCar
from .serializers import VahicleSerializers, CarPartsSerializers, CategorySerializers, TireWheelsSerializers, \
    ExteriorSerializers, lightingSerializers, BodyPartSerializers, InteriorSerializers, AudioSerializers, AutomotiveToolsSerializers, ShopCarSerializers
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import SearchFilter


# Create your views here.


class VahicleViewSet(viewsets.ModelViewSet):
    queryset = VahiclesModel.objects.all()
    serializer_class = VahicleSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['carName']


class CarPartsViewSet(viewsets.ModelViewSet):
    queryset = CarParts.objects.all()
    serializer_class = CarPartsSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['partName']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['CategoryName']


class TireWheelsViewSet(viewsets.ModelViewSet):
    queryset = TireWheels.objects.all()
    serializer_class = TireWheelsSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['TireWheelsName']


class ExteriorViewSet(viewsets.ModelViewSet):
    queryset = Exterior.objects.all()
    serializer_class = ExteriorSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['ExteriorName']


class lightingViewSet(viewsets.ModelViewSet):
    queryset = lighting.objects.all()
    serializer_class = lightingSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['lightingName']
    BodyPartSerializers


class BodyPartViewSet(viewsets.ModelViewSet):
    queryset = BodyPart.objects.all()
    serializer_class = BodyPartSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['BodyPartName']


class InteriorViewSet(viewsets.ModelViewSet):
    queryset = Interior.objects.all()
    serializer_class = InteriorSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['InteriorName']


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['AudioName']


class AutomotiveToolsViewSet(viewsets.ModelViewSet):
    queryset = AutomotiveTools.objects.all()
    serializer_class = AutomotiveToolsSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['AutomotiveToolsName']


class ShopCarViewSet(viewsets.ModelViewSet):
    queryset = ShopCar.objects.all()
    serializer_class = ShopCarSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['AutomotiveToolsName']