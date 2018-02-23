from django.db import models

# Create your models here.


class Post(models.Model):

    name = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        """Return a more readable form of Model object name"""
        return self.name
