from django.urls import path
from apps.users.api import views

urlpatterns = [
    path('', views.ProfileListAPIView.as_view(), name='profile_list_api'),
    path('create/', views.ProfileCreateAPIView.as_view(), name='profile_create_api'),
]