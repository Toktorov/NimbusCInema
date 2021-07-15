from rest_framework import serializers
from apps.movies.models import Movie, MovieImage


class MovieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieImage
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    movie_image = MovieImageSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"