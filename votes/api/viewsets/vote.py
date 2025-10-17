from rest_framework import generics, permissions, serializers
from django.shortcuts import get_object_or_404

from votes.api.serializers.vote import VoteReadSerializer, VoteCreateSerializer, VoteItemSerializer
from votes.models import Vote
from votes.models.vote import VoteItem


class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteCreateSerializer
    permission_classes = [permissions.IsAdminUser]


class VoteItemCreateView(generics.CreateAPIView):
    serializer_class = VoteItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_vote(self):
        vote_id = self.kwargs.get("vote_id")
        return get_object_or_404(Vote, id=vote_id)

    def perform_create(self, serializer):
        vote = self.get_vote()
        employee = self.request.user
        if VoteItem.objects.filter(vote=vote, employee=employee).exists():
            raise serializers.ValidationError("You have already voted for this event")
        serializer.save(vote=vote, employee=employee)


class VoteDetailView(generics.RetrieveAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteReadSerializer
    lookup_field = "id"


class VoteListView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteReadSerializer
