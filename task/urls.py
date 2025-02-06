from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('all_tasks/',views.tasks_list,name='all_tasks'),
    path('create_task/',views.create_task,name='task_create'),
    path('delete_task/<int:id>/',views.delete_task,name='task_delete'),
    path('update_task/<int:id>/',views.update_task,name='task_update')
]
