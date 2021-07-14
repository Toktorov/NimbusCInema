from django.contrib import admin
from apps.movies.models import Movie, MovieImage, Like

# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieImage)
admin.site.register(Like)