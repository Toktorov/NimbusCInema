from django.urls import path
from apps.movies.api import views

urlpatterns = [
    path('', views.MovieListAPIView.as_view(), name='movie_list_api'),
    path('create/', views.MovieCreateAPIView.as_view(), name='movie_create_api'),
    path('image/', views.MovieImageCreateAPIView.as_view(), name='movie_image_create_api')
]