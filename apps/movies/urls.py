from django.urls import path
from apps.movies.views import index, create, detail, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detail<int:id>/', detail, name='detail'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]