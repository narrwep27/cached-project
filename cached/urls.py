from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('register', views.CreateCustomUser.as_view(), name='create_user'),
    path('login', TokenObtainPairView.as_view(), name='token_login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('listusers', views.ListUsers.as_view(), name='read_user_list'),
    path('user/destroy/<int:pk>', views.DestroyUser.as_view(), name='update_user'),
    path('user/read/<int:pk>', views.RetrieveUser.as_view(), name='read_user'),
    path('tag/create', views.CreateTag.as_view(), name='create_tag'),
    path('tag/update/<int:pk>', views.UpdateDestroyTag.as_view(), name='update_tag'),
    path('expense/create', views.CreateExpense.as_view(), name='create_expense'),
    path('expense/update/<int:pk>', views.UpdateDestroyExpense.as_view(), name='update_expense'),
    path('goal/create', views.CreateGoal.as_view(), name='create_goal'),
    path('goal/update/<int:pk>', views.UpdateDestroyGoal.as_view(), name='update_goal'),
]