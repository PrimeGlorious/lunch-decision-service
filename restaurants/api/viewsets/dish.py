from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from restaurants.api.serializers.dish import (
    DishReadSerializer,
    DishSerializer
)
from restaurants.models import Dish


@extend_schema(tags=["Dishes"])
class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return DishReadSerializer
        return DishSerializer
