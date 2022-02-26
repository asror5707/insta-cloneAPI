from django.conf import settings
from django.db import models

class Media(models.Model):
    media = models.FileField(upload_to="post_uchun")

class Post(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    accaunt = models.ForeignKey(settings.ACCOUNT, on_delete=models.CASCADE, related_name='account_posts')
    tag = models.ManyToManyField(settings.ACCOUNT, blank=True, related_name='account_tags')
    matn = models.CharField(max_length=300,blank=True)
    joy = models.CharField(max_length=300,blank=True)
    vaqt = models.DateTimeField(auto_now_add=True)

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    accaunt = models.ForeignKey(settings.ACCOUNT, on_delete=models.CASCADE)

class Saved(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    accaunt = models.ForeignKey(settings.ACCOUNT, on_delete=models.CASCADE)

class Comments(models.Model):
    matn = models.CharField(max_length=150)
    accaunt = models.ForeignKey(settings.ACCOUNT, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vaqt = models.DateTimeField(auto_now_add=True)

class Comment_like(models.Model):
    accaunt = models.ForeignKey(settings.ACCOUNT, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)


class Message(models.Model):
    matn = models.CharField(max_length=150, blank=True)
    yuboruvchi = models.ForeignKey(settings.ACCOUNT, on_delete=models.CASCADE,related_name='message_yuboruvchi')
    qabul = models.ForeignKey(settings.ACCOUNT, on_delete=models.CASCADE, related_name='message_qabul')
    vaqt = models.DateTimeField(auto_now_add=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, blank=True)
