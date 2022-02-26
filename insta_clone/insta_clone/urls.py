
from django.contrib import admin
from django.urls import path
from userapp.views import UserAPIView,UserGDU

from feed.views import PostAPIView,PostGDU,LikeAPIView,MediaAPIView, CommentAPIView, SavedAPIView, \
    Comment_likeAPIView, MessageAPIView,MediaDeleteAPIView,LikeDeleteAPIView

from insta_clone.feed.views import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:pk>/',UserGDU.as_view()),
    path('user/', UserAPIView.as_view()),
    path('post/', PostAPIView.as_view()),
    path('post/<int:pk>/', PostGDU.as_view()),
    path('like/', LikeAPIView.as_view()),
    path('like/<int:pk>/', LikeDeleteAPIView.as_view()),
    path('media/', MediaAPIView.as_view()),
    path('media/<int:pk>/', MediaDeleteAPIView.as_view()),
    path('comment/', CommentAPIView.as_view()),
    path('saved/', SavedAPIView.as_view()),
    path('com_like/', Comment_likeAPIView.as_view()),
    path('message/', MessageAPIView.as_view()),
]
