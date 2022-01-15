from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('todolist/',views.tasklist,name='taskslist'),
    path('todolist/new/', views.task_new, name='task_new'),
    path('todolist/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('todolist/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('todolist/<int:task_id>/',views.taskdetail,name='taskdetail'),
    path('todolist/login/',views.login,name='login'),
    path('todolist/signup/', views.signup,name='signup'),
    path('todolist/logout/',views.logout,name='logout'),
]
