from rest_framework import serializers

from restaurants.models import Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("name", "description")


class DishReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("id", "name", "description")


class DishNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("id", "name")
