from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView
)

from .serializers import (
    DiscussionCreateSerializer,
    CommentsCreateSerializer,
    DiscussionListSerializer,
    DiscussionDetailSerializer,
    CommentsListSerializer,
    CommentDetailSerializer
)

from .models import Discussion, Comments

class DiscussionCreateView(CreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionCreateSerializer

class CommentsCreateView(CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsCreateSerializer

class DiscussionListView(ListAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionListSerializer

class DiscussionDetailView(RetrieveAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionDetailSerializer

class CommentsListView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsListSerializer

class CommentDetailView(RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentDetailSerializer