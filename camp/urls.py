from django.urls import path, include
from rest_framework import routers
from .views import CampData,LocationData

router = routers.DefaultRouter()
router.register(r'',CampData)
# router.register(r'^location',LocationData)


urlpatterns = [
    path("location/", LocationData),
    path("",include(router.urls)),
]