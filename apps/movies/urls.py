from django.urls import path
from apps.movies.views import index, create, detail, update, delete
from apps.users.views import signup, login_user, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:id>/', detail, name='detail'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page= None), name='logout'),
    path('login/', login_user, name='login'),
    path('profile/<username>', profile, name='profile'),
]