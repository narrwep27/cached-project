from django.urls import path
from . import views

urlpatterns = [
    path('read/userlist', views.ReadUserList.as_view(), name='read_user_list'),
    path('read/user/<int:pk>', views.ReadUser.as_view(), name='read_user'),
    path('read/taglist', views.ReadTagList.as_view(), name='read_tag_list'),
    path('read/tag/<int:pk>', views.ReadTag.as_view(), name='read_tag'),
    path('read/expenselist', views.ReadExpenseList.as_view(), name='read_expense_list'),
    path('read/expense/<int:pk>', views.ReadExpense.as_view(), name='read_expense'),
    path('read/goallist', views.ReadGoalList.as_view(), name='read_goal_list'),
    path('read/goal/<int:pk>', views.ReadGoal.as_view(), name='read_goal'),
    path('register', views.CustomUserCreate.as_view(), name='create_user')
]