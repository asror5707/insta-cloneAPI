from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Post, Likes, Comment_like, Comments, Media, Message, Saved


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ["id", 'media', 'accaunt','tag','matn','joy','vaqt']

class LikesSerializer(ModelSerializer):

    class Meta:
        model = Likes
        fields = ["id", 'post', 'accaunt']

class MediaSerializer(ModelSerializer):

    class Meta:
        model = Media
        fields = ["id", 'media']


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comments
        fields = ["id", 'matn', 'accaunt','post','vaqt']

class SavedSerializer(ModelSerializer):

    class Meta:
        model = Saved
        fields = ["id", 'post', 'accaunt']

class Comment_likeSerializer(ModelSerializer):

    class Meta:
        model = Comment_like
        fields = ["id",  'accaunt','comment']

class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = ["id",'matn','yuboruvchi','qabul','vaqt','media']

