from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
    def get_parent(self):
        return self.comment.filter(parent__isnull=True)

    class Meta:
        ordering = ('-created', '-id')

    

class MovieImage(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='post_image'
    )
    image = models.ImageField(
        upload_to='post',
        verbose_name='Картинки'
    )
