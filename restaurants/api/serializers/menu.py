from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from restaurants.api.serializers.dish import DishNameSerializer
from restaurants.api.serializers.restaurant import RestaurantNameSerializer
from restaurants.models import Menu
from restaurants.models.menu import MenuDay


class MenuDaySerializer(ModelSerializer):
    class Meta:
        model = MenuDay
        fields = ["day"]


class MenuSerializer(ModelSerializer):
    days = MenuDaySerializer(many=True, write_only=True)

    class Meta:
        model = Menu
        fields = (
            "name",
            "restaurant",
            "dishes",
            "days",
        )

    def create(self, validated_data):
        days_data = validated_data.pop("days", [])
        dishes_data = validated_data.pop("dishes", [])
        menu = Menu.objects.create(**validated_data)
        menu.dishes.set(dishes_data)
        for day_data in days_data:
            MenuDay.objects.create(menu=menu, **day_data)
        return menu

    def update(self, instance, validated_data):
        days_data = validated_data.pop("days", None)
        dishes_data = validated_data.pop("dishes", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if dishes_data is not None:
            instance.dishes.set(dishes_data)
        if days_data is not None:
            instance.days.all().delete()
            for day_data in days_data:
                MenuDay.objects.create(menu=instance, **day_data)
        return instance


class MenuReadSerializer(ModelSerializer):
    days = SerializerMethodField(read_only=True)
    dishes = DishNameSerializer(many=True, read_only=True)
    restaurant = RestaurantNameSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = (
            "id",
            "name",
            "restaurant",
            "dishes",
            "days",
        )

    def get_days(self, obj):
        return [d.day_name for d in obj.days.all()]
