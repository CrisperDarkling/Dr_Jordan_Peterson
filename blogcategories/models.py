from django.db import models

# Create your models here.
class YoutubeCategory(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
        
