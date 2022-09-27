from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth.decorators import login_required
from base.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', login_required(TaskList.as_view(), login_url='login'), name='tasks'),
    path('task/<int:pk>', login_required(TaskDetail.as_view(), login_url='login'), name='task'),
    path('task-create/', login_required(TaskCreate.as_view(), login_url='login'), name='task-create'),
    path('task-update/<int:pk>', login_required(TaskUpdate.as_view(), login_url='login'), name='task-update'),
    path('task-delete/<int:pk>', login_required(TaskDelete.as_view(), login_url='login'), name='task-delete'),
]
