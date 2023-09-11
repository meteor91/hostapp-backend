from django.urls import include, path, re_path
from rest_framework import routers

from .views import OrdersViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrdersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]