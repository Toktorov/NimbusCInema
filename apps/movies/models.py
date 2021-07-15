from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True
    )

    title = models.CharField(
        max_length=255, blank=True
    )

    en_title = models.CharField(
        max_length=255, blank=True
    )

    description = models.TextField(
        blank=True
    )

    trailer = models.FileField(
        upload_to = 'trailer'
    )
    
    film = models.FileField(
        upload_to = 'film'
    )

    year = models.PositiveIntegerField(
        verbose_name='Год выпуска: ', 
        blank = True, 
        default=2019
    )

    country = models.CharField(
        max_length = 50,
        blank = True
    )

    actors = models.CharField(
        max_length = 255,
        blank = True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

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
        related_name='movie_image'
    )

    image = models.ImageField(
        upload_to='movie',
        verbose_name='Постер'
    )

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_user')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes_movie')


    def __str__(self):
        return f"{self.id}"