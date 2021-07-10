from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(
        max_length=255,
        db_index = True,
        verbose_name = 'Название фильма'
    )

    description = models.TextField(
        verbose_name = 'Описание фильма',
        blank = True, null = True
    )

    def __str__(self):
        return f"{self.title} -- {self.description}"

class MovieImage(models.Model):
    image = models.ImageField(
        upload_to = 'movie',
        verbose_name = 'Постер',
        blank = True, null = True
    )
