from django.urls import path
from apps.comments.api import views

urlpatterns = [
    path('', views.CommentListAPIView.as_view(), name='comment_list_api'),
    path('detail/<int:pk>', views.CommentDetailAPIView.as_view(), name = 'comment_detail_api'),
    path('create/', views.CommentCreateAPIView.as_view(), name='comment_create_api'),
    path('delete/<int:pk>', views.CommentDeleteAPIView.as_view(), name = 'comment_delete_api'),
    path('update/<int:pk>', views.CommentUpdateAPIView.as_view(), name = 'comment_update_api'),
]