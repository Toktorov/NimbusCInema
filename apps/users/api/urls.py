from django.urls import path
from apps.users.api import views

urlpatterns = [
    path('', views.ProfileListAPIView.as_view(), name='profile_list_api'),
    path('detail/<int:pk>', views.ProfileDetailAPIView.as_view(), name = 'profile_detail_api'),
    path('create/', views.ProfileCreateAPIView.as_view(), name='profile_create_api'),
    path('delete/<int:pk>', views.ProfileDeleteAPIView.as_view(), name = 'profile_delete_api'),
    path('update/<int:pk>', views.ProfileUpdateAPIView.as_view(), name = 'profile_update_api'),
]