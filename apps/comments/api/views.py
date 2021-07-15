from rest_framework import generics
from apps.comments.api import serializers
from apps.comments.models import Comment


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
