from django.urls import path, include
from rest_framework import routers

from restaurants.api.viewsets.dish import DishViewSet
from restaurants.api.viewsets.restaurant import RestaurantViewSet

router = routers.DefaultRouter()
router.register(r"restaurants", RestaurantViewSet)
router.register(r"dishes", DishViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "restaurants"
