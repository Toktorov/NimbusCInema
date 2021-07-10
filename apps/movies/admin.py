from django.contrib import admin
from apps.movies.models import Movie, MovieImage

# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieImage)