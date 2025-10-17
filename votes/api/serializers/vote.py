from rest_framework import serializers

from votes.models.vote import VoteItem, Vote


class VoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["restaurant", "vote_date"]


class VoteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteItem
        fields = ["choice"]


class VoteItemReadSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()

    class Meta:
        model = VoteItem
        fields = ["id", "employee", "choice"]


class VoteReadSerializer(serializers.ModelSerializer):
    items = VoteItemReadSerializer(many=True, read_only=True)
    restaurant_name = serializers.CharField(source="restaurant.name")

    class Meta:
        model = Vote
        fields = ["id", "restaurant_name", "vote_date", "items"]
