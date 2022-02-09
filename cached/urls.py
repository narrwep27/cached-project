from django.urls import path
from . import views

urlpatterns = [
    path('register', views.CustomUserCreate.as_view(), name='create_user'),
    path('userlist', views.UserList.as_view(), name='read_user_list'),
    path('user/<int:pk>', views.UserRetrieve.as_view(), name='read_user'),
    path('user/<int:user_id>/createtag', views.CreateTag.as_view(), name='create_user_tag')
]