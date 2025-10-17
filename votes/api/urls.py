from django.urls import path

from votes.api.viewsets.vote import VoteListView, VoteDetailView, VoteItemCreateView, VoteCreateView

urlpatterns = [
    path("create/", VoteCreateView.as_view(), name="vote-create"),
    path("", VoteListView.as_view(), name="vote-list"),
    path("<int:id>/", VoteDetailView.as_view(), name="vote-detail"),
    path("<int:vote_id>/vote/", VoteItemCreateView.as_view(), name="vote-item-create"),
]

app_name = "votes"
