from django.urls import path, include
from rest_framework import routers

from restaurants.api.viewsets.dish import DishViewSet
from restaurants.api.viewsets.menu import MenuViewSet
from restaurants.api.viewsets.restaurant import RestaurantViewSet

router = routers.DefaultRouter()
router.register(r"dishes", DishViewSet)
router.register(r"menus", MenuViewSet)
router.register(r"restaurants", RestaurantViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "restaurants"
