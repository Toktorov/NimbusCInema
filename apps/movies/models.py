from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class MovieImage(models.Model):
    image = models.ImageField(
        upload_to = 'movie',
        verbose_name = 'Постер',
        blank = True, null = True
    )
