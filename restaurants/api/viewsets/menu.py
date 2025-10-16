from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from restaurants.api.serializers.menu import MenuSerializer, MenuReadSerializer
from restaurants.models import Menu


@extend_schema(tags=["Menus"])
class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return MenuReadSerializer
        return MenuSerializer
