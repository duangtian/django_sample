from django.conf.urls import url, include
from django.contrib import admin
from mmdb.views import customerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', customerViewSet)

urlpatterns = [
    url(r'api/', include(router.urls))
]