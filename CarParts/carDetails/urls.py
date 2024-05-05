from django.contrib import admin
from django.urls import path, include
from .views import VahicleViewSet, CarPartsViewSet, CategoryViewSet, TireWheelsViewSet, ExteriorViewSet, lightingViewSet, BodyPartViewSet, InteriorViewSet, AudioViewSet, AutomotiveToolsViewSet, ShopCarViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('Vahicles', VahicleViewSet)
router.register('Parts', CarPartsViewSet)
router.register('Category', CategoryViewSet)
router.register('TireWheels', TireWheelsViewSet)
router.register('Exterior', ExteriorViewSet)
router.register('lighting', lightingViewSet)
router.register('BodyPart', BodyPartViewSet)
router.register('Interior', InteriorViewSet)
router.register('Audio', AudioViewSet)
router.register('AutomotiveTools', AutomotiveToolsViewSet)
router.register('ShopCar', ShopCarViewSet)


urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
