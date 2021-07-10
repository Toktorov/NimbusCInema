from django.urls import path
from apps.movies import views
from apps.movies.views import create_movie

urlpatterns = [
    path('', views.MovieIndexView.as_view(), name = 'index'),
    path('create/', create_movie, name = 'create'),
    path('detail/<int:id>/', views.MovieDetailView.as_view(), name = 'detail'),
]