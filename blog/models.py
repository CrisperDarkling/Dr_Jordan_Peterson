from django.db import models
from django.utils import timezone
from blogcategories.models import YoutubeCategory


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    youtubecategory = models.ForeignKey(YoutubeCategory, blank=True, default="default")
    youtube_link = models.CharField(max_length=500, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post, related_name='comments')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title