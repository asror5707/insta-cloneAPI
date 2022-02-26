from django.shortcuts import render

from .models import Post, Likes, Comment_like, Comments, Media, Message, Saved

from .serializers import PostSerializer, LikesSerializer, MediaSerializer, CommentSerializer, SavedSerializer, \
    Comment_likeSerializer, MessageSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, DestroyAPIView


class PostAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostGDU(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeAPIView(ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

class LikeDeleteAPIView(DestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

class MediaAPIView(CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaDeleteAPIView(DestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    
class CommentAPIView(ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class SavedAPIView(ListCreateAPIView):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer

class Comment_likeAPIView(ListCreateAPIView):
    queryset = Comment_like.objects.all()
    serializer_class = Comment_likeSerializer


class MessageAPIView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer