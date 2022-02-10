from django.urls import path
from . import views

urlpatterns = [
    path('register', views.CreateCustomUser.as_view(), name='create_user'),
    path('listusers', views.ListUsers.as_view(), name='read_user_list'),
    path('user/<int:pk>', views.RetrieveUser.as_view(), name='read_user'),
    path('tag/create', views.CreateTag.as_view(), name='create_tag'),
    path('tag/update/<int:pk>', views.UpdateDestroyTag.as_view(), name='update_destroy_tag'),
    path('expense/create', views.CreateExpense.as_view(), name='create_expense')
]