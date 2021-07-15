from django.urls import path
from apps.comments.api import views

urlpatterns = [
    path('', views.CommentListAPIView.as_view(), name='comment_list_api'),
    path('create/', views.CommentCreateAPIView.as_view(), name='comment_create_api'),
]