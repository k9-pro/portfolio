from django.urls import path, include
from rest_framework import routers
from .views import CampData

router = routers.DefaultRouter()
router.register(r'',CampData)

urlpatterns = [
    path("",include(router.urls)),
]