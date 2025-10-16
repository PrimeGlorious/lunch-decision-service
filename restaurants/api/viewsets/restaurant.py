from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from restaurants.api.serializers.restaurant import (
    RestaurantReadSerializer,
    RestaurantSerializer,
)
from restaurants.models import Restaurant


@extend_schema(tags=["Restaurants"])
class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return RestaurantReadSerializer
        return RestaurantSerializer
