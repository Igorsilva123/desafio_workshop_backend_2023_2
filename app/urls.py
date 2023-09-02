from django.conf import settings
from rest_framework import routers
from .views import *
from django.urls import path

router = routers.DefaultRouter()
router.register(r'marcas', MarcasView)
router.register(r'carros', CarrosView)
urlpatterns = []
urlpatterns += router.urls