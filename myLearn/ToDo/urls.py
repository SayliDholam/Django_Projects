from django.urls import path
from .views import task_list, add_task, update_status, delete_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('update/<int:task_id>/<str:status>/', update_status, name='update_status'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]