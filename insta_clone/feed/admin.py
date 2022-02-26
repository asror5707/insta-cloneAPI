from django.contrib import admin
from .models import Media,Post, Likes, Saved, Comments, Comment_like, Message
admin.site.register(Media)
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Saved)
admin.site.register(Comments)
admin.site.register(Comment_like)
admin.site.register(Message)
